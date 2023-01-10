FROM python:3

ADD main.py /
ADD requirements.txt /

RUN pip install -r /requirements.txt

ENTRYPOINT [ "python3", "/main.py" ]
