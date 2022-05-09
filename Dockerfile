FROM python:3.8

RUN apt-get update \
    && apt-get install -y open-jtalk open-jtalk-mecab-naist-jdic
