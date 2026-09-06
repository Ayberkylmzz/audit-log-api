from datetime import datetime

from pydantic import BaseModel


class AuditLogCreate(BaseModel):
    actor: str
    action: str
    resource: str


class AuditLogRead(BaseModel):
    id: int
    actor: str
    action: str
    resource: str
    timestamp: datetime
