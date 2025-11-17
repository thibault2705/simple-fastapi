"""
 Module Name: greeting.py
 Author: thibault2705
 Date: 2025-11-16
 Description: Greeting API v1
 """

from fastapi import APIRouter
from loguru import logger

logger.debug(f"Initializing API")

router = APIRouter()
router = APIRouter(prefix="/greeting", tags=["v1/greeting"])

@router.get("/{name}")
def greet(name: str):
    logger.info(f"Greeting {name}")
    return f"Hello, {name}! This is a greeting from API v1."