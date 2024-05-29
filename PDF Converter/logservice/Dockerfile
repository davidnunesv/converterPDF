FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 8083
CMD ["python", "log_service.py"]
