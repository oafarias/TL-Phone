# Ajuste 1: Atualizando para Python 3.12 (Padrão da Stack)
FROM python:3.12-slim

# Configurações para não gerar lixo (.pyc) e logs imediatos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Pasta de trabalho
WORKDIR /app

# Instala dependências do sistema (gcc e libpq para o PostgreSQL)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala as bibliotecas do projeto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código todo
COPY . /app/

# Expõe a porta 8000
EXPOSE 8000

# Ajuste 2: Usando Gunicorn em vez de runserver para Produção
# 'setup.wsgi' deve ser substituído pelo nome da pasta onde o settings.py for criado (veja abaixo)
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]