FROM python:3.10.8-slim

WORKDIR /app/
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

ENV DEBUG=False

CMD [ "gunicorn", "--bind=0.0.0.0:80", "--workers=4", "user.wsgi" ]