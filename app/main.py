from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
import uvicorn

app = FastAPI()
requests_counter = Counter('http_requests_total', 'Total HTTP requests')

@app.get("/health")
def health():
    requests_counter.inc()
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    requests_counter.inc()
    return generate_latest()

@app.post("/echo")
def echo(data: dict):
    requests_counter.inc()
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)