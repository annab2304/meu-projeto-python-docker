# Imagem base do Python
FROM python:3.10-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependência
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar o restante do projeto
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
