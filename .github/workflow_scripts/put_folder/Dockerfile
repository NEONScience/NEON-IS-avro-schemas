# Dockerfile with Pachyderm Python library

FROM python:3.10

# maintainer handle
MAINTAINER "Cove Sturtevant" csturtevant@battelleecology.org

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./put_folder.py .

RUN [ "python", "./put_folder.py" ]