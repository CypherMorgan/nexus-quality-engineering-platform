from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import Base
from app.database import SessionLocal
from app.database import engine
from app.models import User

app = FastAPI(
    title="Nexus QE Mock Service"
)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/users/{user_id}")
def get_user(
    user_id: int,
):
    db: Session = SessionLocal()

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    return {
        "id": user.id,
        "username": user.username,
    }


@app.get(
    "/login",
    response_class=HTMLResponse,
)
def login_page():
    return Path(
        "app/templates/login.html"
    ).read_text()


@app.get(
    "/dashboard",
    response_class=HTMLResponse,
)
def dashboard_page():
    return Path(
        "app/templates/dashboard.html"
    ).read_text()