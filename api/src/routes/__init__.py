from fastapi import APIRouter
from core.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from . import blog_router, user_router

router = APIRouter(prefix="/api")


router.include_router(blog_router.router)
router.include_router(user_router.router)
