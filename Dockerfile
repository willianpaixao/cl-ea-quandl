FROM python:3.8

LABEL org.opencontainers.image.authors="Willian Paixao <willian@ufpa.br>"
LABEL org.opencontainers.image.source="https://github.com/willianpaixao/cl-ea-quandl"

ARG created
ARG revision
ARG version=local
ENV CREATED=$created
ENV REVISION=$revision
ENV VERSION=$version
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get install --yes curl

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt
COPY . .

USER nobody

EXPOSE 1717/tcp
EXPOSE 5000/tcp

ENTRYPOINT [ "uwsgi" ]
CMD [ "--yaml", "uwsgi.yml" ]

HEALTHCHECK CMD curl -f http://localhost:5000/healthcheck || exit 1
