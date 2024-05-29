FROM alpine:latest
RUN apk add --no-cache ghostscript
WORKDIR /app
COPY . .
EXPOSE 8081
CMD ["sh", "-c", "while true; do sleep 1000; done"]
