FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1

CMD ["flask", "run"]
