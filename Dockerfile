FROM registry.opensuse.org/opensuse/leap:15.3

RUN zypper ref && zypper install -y python3 python3-pip

RUN mkdir /app
WORKDIR /app
COPY src/* . /app/
RUN pip3 install -r requirements.txt

EXPOSE 8081
CMD ["python3", "/app/main.py"]
