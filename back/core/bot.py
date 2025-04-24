from dataclasses import dataclass
from typing import List
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from .config import settings
from .custom_pg_vector import CustomPGVector


@dataclass
class Bot:
    __connection = CustomPGVector(
        embeddings=OllamaEmbeddings(model="mxbai-embed-large"),
        collection_name=settings.database_collection_name,
        connection=settings.database_url,
        use_jsonb=True,
    )

    def __get_data(self, query: str) -> List[Document]:
        results = self.__connection.similarity_search(query)
        return results

    def __template(self, query: str) -> str:
        template = """
        Eres asistente en tareas de preguntas y respuestas. Usa los siguientes fragmentos de contexto para responder la pregunta. Si no sabes la respuesta, simplemente di que no la sabes. Mantén la respuesta concisa.
        question: {question}
        context: {context}
        Answer:
        """

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | OllamaLLM(model="llama3.2")
        results = self.__get_data(query)
        return chain.invoke(
            {
                "question": query,
                "context": "\n".join([doc.page_content for doc in results]),
            }
        )

    def invoke(self, query: str) -> str:
        return self.__template(query)
