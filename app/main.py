from pathlib import Path

from fastapi import FastAPI, HTTPException
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

def seed_database() -> None:
    db: Session = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(User.id == 1)
        .first()
    )

    if existing_user:
        db.close()
        return

    demo_user = User(
        id=1,
        username="demo",
    )

    db.add(demo_user)
    db.commit()
    db.close()

seed_database()

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

@app.get(
    "/login",
    response_class=HTMLResponse,
)
def login_page():
    return Path(
        "app/templates/login.html"
    ).read_text(
        encoding="utf-8"
    )

@app.get(
    "/dashboard",
    response_class=HTMLResponse,
)
def dashboard_page():
    return Path(
        "app/templates/dashboard.html"
    ).read_text(
        encoding="utf-8"
    )