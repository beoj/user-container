FROM python:3.10.8-slim

WORKDIR /app/
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

ENV DEBUG=False
ENV HOST=localhost
ENV PORT=27017
ENV USER=admin
ENV PASSWORD=admin

CMD [ "gunicorn", "--bind=0.0.0.0:80", "--workers=4", "user.wsgi" ]