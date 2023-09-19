FROM python:3.11

WORKDIR /usr/src/app

RUN pip install --no-cache-dir selenium

COPY router_reboot.py .

CMD [ "python", "./router_reboot.py"]
