FROM alpine:latest

RUN apk add --no-cache bash git python py-pip alpine-sdk && \
    git clone https://github.com/Gadgetoid/Pinout.xyz.git /usr/share/Pinout.xyz && \
    cd /usr/share/Pinout.xyz && \
    pip install -r requirements.txt

EXPOSE 5000

ADD init.py /init.py

WORKDIR /usr/share/Pinout.xyz
CMD ["python", "/init.py"]
