from fastapi import APIRouter

router = APIRouter(prefix="/greeting", tags=["v1/greeting"])

@router.get("/{name}")
def greet(name: str):
    return f"Hello, {name}! This is a greeting from API v1."