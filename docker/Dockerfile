FROM python:3.6.2

WORKDIR /root
ADD requirements.txt /root
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install graphviz

WORKDIR /src
ADD src/ /src

CMD ["python", "server.py"]

