from datetime import datetime

_logs: list[dict] = []
_next_id = 1


def add(actor: str, action: str, resource: str) -> dict:
    global _next_id

    log = {
        "id": _next_id,
        "actor": actor,
        "action": action,
        "resource": resource,
        "timestamp": datetime.now(),
    }
    _logs.append(log)
    _next_id += 1
    return log


def get_all() -> list[dict]:
    return _logs


def get_by_id(log_id: int) -> dict | None:
    for log in _logs:
        if log["id"] == log_id:
            return log
    return None
