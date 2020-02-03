FROM python:3

RUN apt update
RUN apt-get install -y mecab mecab-ipadic-utf8 libmecab-dev swig groff-base less

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install mecab-python3==0.7
