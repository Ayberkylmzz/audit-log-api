from app.repositories import audit_log_repository
from app.schemas.audit_log import AuditLogCreate


def create_log(data: AuditLogCreate) -> dict:
    return audit_log_repository.add(
        actor=data.actor,
        action=data.action,
        resource=data.resource,
    )


def list_logs() -> list[dict]:
    return audit_log_repository.get_all()


def get_log(log_id: int) -> dict | None:
    return audit_log_repository.get_by_id(log_id)
