from pathlib import Path

from fastapi import FastAPI, HTTPException
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


@app.post("/auth/login")
def login(payload: dict):
    username = payload.get("username")
    password = payload.get("password")

    if (
        username == "demo"
        and password == "password"
    ):
        return {
            "token": "mock-jwt-token",
            "username": username,
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials",
    )


@app.get("/users/{user_id}")
def get_user(user_id: int):
    db: Session = SessionLocal()

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "id": user.id,
        "username": user.username,
    }


@app.get("/login")
def login_page():
    return Path(
        "app/templates/login.html"
    ).read_text()


@app.get("/dashboard")
def dashboard_page():
    return Path(
        "app/templates/dashboard.html"
    ).read_text()