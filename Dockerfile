FROM python:buster

# ENV SRV_PORT=4300
ENV SRV_DEBUG=True
ENV SRV_HOST=0.0.0.0
ENV SRV_PORT=80
ENV FLASK_APP=app
ENV DB_STRING=mysql+pymysql://root:root@mysql:3306/bdd_projet

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "-m", "src"]