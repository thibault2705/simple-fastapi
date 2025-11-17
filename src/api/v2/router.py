"""
 Module Name: router.py
 Author: thibault2705
 Date: 2025-11-16
 Description: API v2 Router
 """

from fastapi import APIRouter
from loguru import logger

logger.debug(f"Initializing router")

from . import random_api as v2_random_api


# Initialize router
router = APIRouter(
    prefix="/v2",
    tags=["v2"],
    responses={
        404: {"description": "Not found in v2."}
    },
)

router.include_router(v2_random_api.router)
