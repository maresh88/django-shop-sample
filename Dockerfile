FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install --upgrade pip wheel
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary
