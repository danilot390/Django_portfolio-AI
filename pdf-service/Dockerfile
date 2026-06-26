FROM mcr.microsoft.com/playwright:v1.50.0-noble

WORKDIR /app

COPY package*.json ./

RUN npm ci

RUN npx playwright install --with-deps

COPY . .

EXPOSE 3001

CMD ["npm", "start"] 