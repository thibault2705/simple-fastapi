import random

from fastapi import APIRouter, HTTPException, Query
from typing import Annotated

router = APIRouter(tags=["v2/random"])

@router.get("/random/{max_value}")
def gen_random_int(max_value: int):
    return {
        "max_value": max_value,
        "random_number": random.randint(1, max_value)
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
        raise HTTPException(status_code=400, detail="min_value can't be greater than max_value")

    return {
        "min_value": min_value,
        "max_value": max_value,
        "random_number": random.randint(min_value, max_value)
    }