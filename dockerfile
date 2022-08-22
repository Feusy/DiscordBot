#Get last python
FROM python:3.8-slim-buster
WORKDIR /

COPY . .

RUN pip install python-dotenv
RUN pip install discord 
RUN pip install webscrape
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install lxml

CMD [ "python", "./bot.py" ]