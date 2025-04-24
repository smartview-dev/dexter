from langchain_postgres import PGVector
from langchain_core.documents import Document
from typing import List, Optional, Dict, Any


class CustomPGVector(PGVector):
    def __init__(self, *, user_id: str, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id

    def add_texts(
        self, texts: List[str], metadatas: Optional[List[dict]] = None, **kwargs
    ) -> List[str]:
        if metadatas:
            for meta in metadatas:
                meta.update({"user_id": self.user_id})
        else:
            metadatas = [{"user_id": self.user_id} for _ in texts]

        return super().add_texts(texts, metadatas, **kwargs)

    def add_documents(
        self,
        documents: List[Document],
        **kwargs: Any,
    ) -> List[str]:
        processed_docs = []
        for doc in documents:
            new_metadata = {
                "user_id": self.user_id,
                **(doc.metadata or {}),
            }
            processed_docs.append(
                Document(page_content=doc.page_content, metadata=new_metadata)
            )
        return super().add_documents(processed_docs, **kwargs)

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        filter: Optional[Dict] = None,
        **kwargs: Any,
    ) -> List[Document]:
        custom_filter = {"user_id": self.user_id}
        merged_filter = {**custom_filter, **(filter or {})}

        self._filter_template = """
            metadata->>'user_id' = :user_id
            {existing_filter}
        """

        return super().similarity_search(
            query=query, k=k, filter=merged_filter, **kwargs
        )
