FROM python:buster

# ENV SRV_PORT=4300
ENV SRV_DEBUG=True
ENV SRV_HOST=0.0.0.0
ENV SRV_PORT=80
ENV FLASK_APP=app
ENV DB_STRING=mysql://root:root@host.docker.internal/app

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "-m", "src"]