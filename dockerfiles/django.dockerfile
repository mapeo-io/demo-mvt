FROM ubuntu:jammy-20240911.1

WORKDIR /app

RUN apt-get update
RUN apt-get install gdal-bin -y
RUN apt-get install libgdal-dev -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-setuptools -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./environment/requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./geodjango_mvt/ .

EXPOSE 8000

RUN chmod +x /app/start.sh

ENTRYPOINT ["./start.sh"]