from fastapi import APIRouter

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
