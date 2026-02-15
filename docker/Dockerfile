FROM python:3.11-slim

WORKDIR /app

# Copia requirements primeiro (cache de layers)
COPY requirements.txt .

# Instala tudo, incluindo uvicorn explicitamente
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "uvicorn[standard]"

# Copia o resto do código
COPY . .

# Porta que a app escuta
EXPOSE 8000

# Comando correto (ajuste "main:app" para o seu arquivo real, ex: app.main:app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
