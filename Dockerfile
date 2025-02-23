FROM python:3.13-slim

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]