from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(
    title="Netflix Clone API",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Backend",
        "version": "0.1.0"
    }

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db": "connected", "result": result.scalar()}
