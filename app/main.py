from fastapi import FastAPI

from app.api import audit_logs, health

app = FastAPI(title="Audit Log API")

app.include_router(health.router)
app.include_router(audit_logs.router)
