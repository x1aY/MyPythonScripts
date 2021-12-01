FROM python:3.7
MAINTAINER xy

COPY requirements.txt /requirements.txt

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /MyScripts

EXPOSE 7979

CMD python MyScripts/app.py
