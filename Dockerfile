FROM ubuntu:14.04
MAINTAINER jcdoll
EXPOSE 5000

RUN apt-get -qq update
RUN apt-get -qqy install python python-dev python-pip

# Fix pip/requests IncompleteRead bug
RUN sudo rm -rf /usr/local/lib/python2.7/dist-packages/requests

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD paperbot.py /code/
CMD python paperbot.py
