from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import blog_crud
from core.pydantic_schema import blog_schema
from core.routes import get_db

router = APIRouter(prefix="/blog")


@router.get("/", response_model=list[blog_schema.Blog])
async def root(db: Session = Depends(get_db)):
    blogs = blog_crud.get_blogs(db)
    return blogs


@router.get("/{blog_id}", response_model=blog_schema.Blog)
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = blog_crud.get_blog(db, blog_id)
    return blog


@router.post("/create", response_model=blog_schema.Blog)
async def create_blog(blog: blog_schema.BlogCreate, db: Session = Depends(get_db)):
    blog = blog_crud.create_blog(db, blog)
    return blog


@router.put("/{blog_id}", response_model=blog_schema.Blog)
async def update_blog(
    blog_id: int, blog: blog_schema.BlogCreate, db: Session = Depends(get_db)
):
    blog = blog_crud.update_blog(db, blog_id, blog)
    return blog


@router.delete("/{blog_id}")
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = blog_crud.delete_blog(db, blog_id)
    return blog
