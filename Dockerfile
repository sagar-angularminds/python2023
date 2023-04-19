# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim-buster

WORKDIR /src

COPY src/ .

COPY requirements.txt requirements.txt

RUN pip3 freeze > requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["sh","startup.sh"]
