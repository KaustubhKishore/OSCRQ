FROM node

WORKDIR /usr/src/app

COPY Dashboard/package*.json ./

RUN npm install

COPY Dashboard .

CMD ["node", "index.js"]