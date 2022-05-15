FROM python:3.9

ARG OPENJTALK_VERSION=1.11

RUN apt-get update \
    && apt-get install -y \
    open-jtalk \
    open-jtalk-mecab-naist-jdic \
    curl \
    unzip

RUN mkdir -p /usr/share/open_jtalk/voices/mei /usr/share/open_jtalk/voices/takumi /usr/share/open_jtalk/voices/slt \
    && curl -SLO https://downloads.sourceforge.net/project/mmdagent/MMDAgent_Example/MMDAgent_Example-1.8/MMDAgent_Example-1.8.zip \
    && unzip MMDAgent_Example-1.8.zip \
    && cp MMDAgent_Example-1.8/Voice/mei/*.htsvoice /usr/share/open_jtalk/voices/mei/ \
    # && cp MMDAgenut_Example-1.8/Voice/slt/*.htsvoice /usr/share/open_jtalk/voices/slt/ \
    && cp MMDAgent_Example-1.8/Voice/takumi/*.htsvoice /usr/share/open_jtalk/voices/takumi/

RUN pip install -U pip poetry

WORKDIR /usr/src/pyjtalk

ENV POETRY_VIRTUALENVS_CREATE=false
COPY pyproject.toml poetry.lock /usr/src/pyjtalk/
COPY pyjtalk/ /usr/src/pyjtalk/pyjtalk
RUN poetry install

ENTRYPOINT ["python3", "-m", "pyjtalk"]
CMD [ "こんにちは" ]
