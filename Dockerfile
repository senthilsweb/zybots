FROM python:3.8-slim-buster

# install utilities
RUN apt-get update && apt-get -y install sudo && apt-get install curl -y
RUN pip install gunicorn

WORKDIR /src
COPY ./docx .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["gunicorn"  , "-b", "0.0.0.0:3000", "resources.api:app"]