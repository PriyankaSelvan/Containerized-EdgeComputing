FROM python:2.7.14-alpine3.7

WORKDIR .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/numberserver/app.py" ]
