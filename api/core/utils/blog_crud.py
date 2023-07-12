from sqlalchemy.orm import Session

from core.db import blog_model
from core.pydantic_schema import blog_schema


def get_blogs(db: Session) -> list[blog_model.Blog]:
    return db.query(blog_model.Blog).all()


def get_blog(db: Session, blog_id: int) -> blog_model.Blog:
    return db.query(blog_model.Blog).filter(blog_model.Blog.id == blog_id).first()


def create_blog(db: Session, blog: blog_schema.BlogCreate) -> blog_model.Blog:
    db_blog = blog_model.Blog(title=blog.title, body=blog.body)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_blog(db: Session, blog_id: int, blog: blog_schema.Blog) -> blog_model.Blog:
    db_blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == blog_id).first()
    db_blog.title = blog.title
    db_blog.body = blog.body
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db: Session, blog_id: int) -> None:
    db.query(blog_model.Blog).filter(blog_model.Blog.id == blog_id).delete()
    db.commit()
