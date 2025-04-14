# Etapa 1: Construcción de la aplicación Angular
FROM node:latest AS build

# Instalar pnpm globalmente
RUN npm install -g pnpm

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de declaración de dependencias para aprovechar el cacheo
COPY package.json pnpm-lock.yaml ./

# Instalar dependencias con pnpm
RUN pnpm install

# Copiar el resto de la aplicación
COPY . .

# Construir la aplicación Angular en modo producción
RUN ng build

# Etapa 2: Servir la aplicación con Nginx
FROM nginx:latest

# Copiar la configuración personalizada de Nginx (opcional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Copiar los archivos compilados desde la etapa build
# Asegúrate de reemplazar <nombre-del-proyecto> por el nombre correcto que se genere en la carpeta dist
COPY --from=build /app/dist/front /usr/share/nginx/html

# Exponer el puerto en el que correrá Nginx
EXPOSE 80

# Comando para iniciar Nginx en primer plano
# CMD ["nginx", "-g", "daemon off;"]
