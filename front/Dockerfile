# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:18 as build-stage

WORKDIR /app

COPY ./nginx.conf /nginx.conf

RUN curl -sL https://unpkg.com/@pnpm/self-installer | node

COPY package*.json /app/

RUN pnpm install

COPY ./ /app/

RUN pnpm run build


# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15

COPY --from=build-stage /app/dist/ /usr/share/nginx/html

COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
