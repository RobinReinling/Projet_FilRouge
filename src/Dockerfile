FROM python

WORKDIR /app

EXPOSE 8081

COPY . .

RUN pip install -r requirements.txt

CMD ["flask","run","--host=0.0.0.0"]