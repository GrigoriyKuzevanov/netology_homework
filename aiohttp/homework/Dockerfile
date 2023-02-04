FROM python:3.11

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "python", "app.py" ]