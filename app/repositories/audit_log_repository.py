from app.core.database import get_connection

def add(actor: str, action: str, resource: str) -> dict:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO audit_logs (actor, action, resource)
        VALUES (%s,%s,%s)
        RETURNING id, actor, action, resource, timestamp
        """,
        (actor, action, resource),
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {
        "id": row[0],
        "actor": row[1],
        "action": row[2],
        "resource": row[3],
        "timestamp": row[4],
    }


def get_all() -> list[dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, actor, action, resource, timestamp FROM audit_logs ORDER BY id"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "id": row[0],
            "actor": row[1],
            "action": row[2],
            "resource": row[3],
            "timestamp": row[4],
        }
        for row in rows
    ]


def get_by_id(log_id: int) -> dict | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, actor, action, resource, timestamp FROM audit_logs WHERE id = %s",
        (log_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        return None
    return {
        "id": row[0],
        "actor": row[1],
        "action": row[2],
        "resource": row[3],
        "timestamp": row[4],
    }
