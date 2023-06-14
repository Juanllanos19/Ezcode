FROM node:18-alpine3.18

RUN npm install -g http-server
    
RUN mkdir /Front

WORKDIR /Front

COPY package.json ./

RUN npm cache clean --force

RUN rm -rf node_modules

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["http-server", "dist"]