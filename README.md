# Converter PDF
Criação de um conversor de PDF para txt e PDF reducer
Este projeto é uma criação com serviços realizados em containers Docker, com um Docker Compose para manipular a ordem dos serviços, portas e chamadas. Cada serviço ficará e uma porta, em nosso caso estará descrito nos serviços a baixo.
# PDF Reducer
Serviço com função de reduzir a resolução de um arquivo no formato PDF. (Porta 8081)
# PDF to Text
Serviço com função de converter um PDF para texto. (Porta 8082)
# Logs
Serviço com função de registrar as operações dos outros serviços. (Porta 8083)
