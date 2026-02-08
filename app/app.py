from fastapi import FastAPI
from app.logging_config import setup_logging

logger = setup_logging()

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}