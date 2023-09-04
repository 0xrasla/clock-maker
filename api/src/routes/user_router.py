from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/")
async def root():
    return {"message": "Hello from user!"}


@router.get("/ping")
async def ping():
    return {"message": "pong"}
