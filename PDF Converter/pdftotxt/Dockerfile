FROM alpine:latest
RUN apk add --no-cache poppler-utils
WORKDIR /app
COPY . .
EXPOSE 8082
CMD ["sh", "-c", "while true; do sleep 1000; done"]
