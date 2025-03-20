FROM python:3.12.0


ENV HOME=/home/RabbitMQ \
    APP_HOME=$HOME/app \
    PYTHONPATH="$PYTHONPATH:$HOME" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY publisher.py .









