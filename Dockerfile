FROM python:3

ADD Main.py /

RUN pip install pystrich

CMD [ "python", "./Main.py" ]