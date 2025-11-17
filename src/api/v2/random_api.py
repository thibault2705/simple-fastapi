import random

from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
from loguru import logger

logger.debug(f"Initializing API")

router = APIRouter(tags=["v2/random"])

@router.get("/random/{max_value}")
def gen_random_int(max_value: int):
    random_value = gen_random(1, max_value)

    return {
        "max_value": max_value,
        "random_number": random_value
    }

@router.get("/random-in-range")
def gen_random_in_range(
        min_value: Annotated[int, Query(
            title="Minimum Value",
            description="The minimum random number",
            ge=0,
            le=1000
        )] = 0,
        max_value: Annotated[int, Query(
            title="Maximum Value",
            description="The maximum random number",
            ge=1,
            le=1000
        )] = 100
    ):

    if min_value > max_value:
        logger.exception(
            f"min_value {min_value} is greater max_value {max_value}")
        raise HTTPException(status_code=400, detail="min_value can't be greater than max_value")

    random_value = gen_random(min_value, max_value)
    return {
        "min_value": min_value,
        "max_value": max_value,
        "random_number": random_value
    }

def gen_random(min_value: int, max_value: int):
    random_value = random.randint(min_value, max_value)

    logger.info(f"Random value {random_value} generated, min_value = {min_value}, max_value = {max_value}")

    return random_value