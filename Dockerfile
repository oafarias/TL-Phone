# Usa Python leve
FROM python:3.10-slim

# Configurações para não gerar lixo (.pyc)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Pasta de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Instala as bibliotecas do projeto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código todo
COPY . /app/

# Expõe a porta 8000
EXPOSE 8000

# Comando de partida
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]