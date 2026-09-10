from fastapi import APIRouter, HTTPException

from app.schemas.audit_log import AuditLogCreate, AuditLogRead
from app.services import audit_log_service

router = APIRouter(prefix="/logs", tags=["logs"])


@router.post("", response_model=AuditLogRead, status_code=201)
def create_log(data: AuditLogCreate):
    return audit_log_service.create_log(data)


@router.get("", response_model=list[AuditLogRead])
def list_logs(actor: str | None = None, limit: int = 50, offset: int = 0):
    return audit_log_service.list_logs(actor=actor, limit=limit, offset=offset)


@router.get("/{log_id}", response_model=AuditLogRead)
def get_log(log_id: int):
    log = audit_log_service.get_log(log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log
