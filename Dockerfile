FROM python:3.8-buster

WORKDIR /workspace/
COPY requirements.txt /workspace/
COPY .bashrc /root/


RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y default-jre default-jdk \
 && pip install -r requirements.txt

# コンテナ起動時に実行するコマンドを指定
ENTRYPOINT ["/workspace/.bashrc"]