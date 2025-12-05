from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import FRONTEND_URL
from database import engine
from todos import router as todos_router
from logger import logger


app = FastAPI()


@app.on_event("startup")
def startup():
    logger.info("Server started!")


@app.on_event("shutdown")
def shutdown():
    engine.dispose()
    logger.info("Server shutdown!")


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["Content-Type", "X-API-Key"],
)

# Include routers
app.include_router(todos_router)
