FROM node:16-alpine3.17

RUN npm install -g http-server
    
RUN mkdir /app

WORKDIR /Front

COPY package.json ./

RUN npm install

COPY . .

RUN npm run dev

EXPOSE 9005

CMD ["http-server", "dist"]

