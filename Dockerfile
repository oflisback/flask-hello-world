FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y python3-pip python-dev python3-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
COPY ./version.txt /app/version.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
