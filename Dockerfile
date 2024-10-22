FROM python:3.8-slim

WORKDIR /app

COPY requeriments.txt /app
RUN pip install -r requeriments.txt


ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "app", "--host=172.0..1"]