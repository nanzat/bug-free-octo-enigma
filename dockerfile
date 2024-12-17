FROM python:3.10-slim
ENV TOKEN='add your token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]

