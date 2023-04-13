# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:2.7

WORKDIR /app
COPY app/ ./app/

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["sh", "/app/app/startup.sh"]
