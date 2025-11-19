FROM python:3.11-slim
WORKDIR /app
COPY hello.py .
RUN pip install --no-cache-dir --upgrade pip
EXPOSE 8080
CMD ["python", "hello.py"]
