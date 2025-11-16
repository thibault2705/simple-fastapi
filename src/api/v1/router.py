from fastapi import APIRouter

from . import greeting_api as v1_greeting_api

# Initialize router
router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={
        404: {"description": "Not found in v1."}
    },
)

router.include_router(v1_greeting_api.router)
