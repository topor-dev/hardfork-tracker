FROM python:3.6.8-alpine3.9

WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./hardfork ./hardfork
ENTRYPOINT ["python3", "-m", "hardfork"]
