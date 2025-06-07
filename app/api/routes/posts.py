from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.post import (create_post, delete_post, get_post, get_posts,
                           update_post)
from app.database.deps import get_db
from app.schemas.post import PostCreate, PostOut, PostUpdate

post_router = APIRouter()


@post_router.get("/posts", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return get_posts(db)


@post_router.post("/posts", response_model=PostOut)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)


@post_router.get("/posts/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@post_router.put("/posts/{post_id}", response_model=PostOut)
def update_existing_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    updated = update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated


@post_router.delete("/posts/{post_id}")
def delete_existing_post(post_id: int, db: Session = Depends(get_db)):
    deleted = delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"ok": True}
