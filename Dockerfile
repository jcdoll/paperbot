FROM ubuntu:14.04
MAINTAINER jcdoll
EXPOSE 5000

RUN apt-get -qq update
RUN apt-get -qqy install python python-dev python-pip

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD paperbot.py /code/
CMD python paperbot.py
