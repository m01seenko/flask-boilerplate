FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY . /opt/app
WORKDIR /opt/app

RUN pip install --no-cache-dir flake8 && flake8 \
 && pip install --no-cache-dir -r requirements.txt

CMD ["/bin/sh", "./docker-entry.sh"]
