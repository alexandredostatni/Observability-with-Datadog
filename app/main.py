# app/main.py
from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter, Histogram, Summary
import time

app = FastAPI()

# Cria o app ASGI do Prometheus
metrics_app = make_asgi_app()

# Monta o endpoint /metrics
app.mount("/metrics", metrics_app)

# Exemplos de métricas customizadas (opcional, mas recomendado)
REQUESTS = Counter('http_requests_total', 'Total de requisições HTTP', ['method', 'endpoint'])
REQUEST_TIME = Histogram('http_request_duration_seconds', 'Tempo de requisição em segundos', ['method', 'endpoint'])

@app.middleware("http")
async def add_prometheus_metrics(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    REQUESTS.labels(method=request.method, endpoint=request.url.path).inc()
    REQUEST_TIME.labels(method=request.method, endpoint=request.url.path).observe(duration)

    return response

# Suas rotas normais
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "ok"}