from fastapi import FastAPI

import uvicorn

# Import the router instance from your V1 file
from src.api.v1.router import router as v1_router
from src.api.v2.router import router as v2_router


app = FastAPI(
    title="My Versioned API",
    description="This is the main application.",
)

app.include_router(v1_router, prefix="/api")
app.include_router(v2_router, prefix="/api")

@app.get("/")
def home():
    return "Hi, there. This is the homepage."


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)