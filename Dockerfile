FROM python:3.8

LABEL org.opencontainers.image.authors="Willian Paixao <willian@ufpa.br>"

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get install --yes curl

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000/tcp

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

HEALTHCHECK CMD curl -f http://localhost:5000/healthcheck || exit 1
