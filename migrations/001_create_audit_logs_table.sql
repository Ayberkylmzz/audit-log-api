CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    actor TEXT NOT NULL,
    action TEXT NOT NULL,
    resource TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);