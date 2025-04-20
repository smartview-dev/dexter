FROM node:22.14.0-alpine AS build

RUN npm install -g pnpm

WORKDIR /app

COPY package.json pnpm-lock.yaml ./
COPY src src
COPY angular.json tsconfig.json tsconfig.app.json ./

RUN pnpm install --frozen-lockfile && \
  pnpm run build -- --configuration production --output-path=dist/browser

FROM nginx:1.27.5-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/dist/browser /usr/share/nginx/html

RUN chmod -R 755 /usr/share/nginx/html && \
  chown -R nginx:nginx /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
