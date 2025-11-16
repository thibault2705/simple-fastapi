import random
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query

import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return "Hi, there"

@app.get("/greeting/{name}")
def greet(name: str):
    return f"Hello, {name}!"

@app.get("/random/{max_value}")
def gen_random_int(max_value: int):
    return {
        "max_value": max_value,
        "random_number": random.randint(1, max_value)
    }

@app.get("/random-in-range")
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)