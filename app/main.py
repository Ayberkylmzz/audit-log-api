import psycopg
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import audit_logs, health

app = FastAPI(title="Audit Log API")

app.include_router(health.router)
app.include_router(audit_logs.router)


@app.exception_handler(psycopg.OperationalError)
def handle_db_connection_error(request: Request, exc: psycopg.OperationalError):
    return JSONResponse(
        status_code=503,
        content={"detail": "Veritabanına bağlanılamıyor, lütfen daha sonra tekrar deneyin."},
    )
