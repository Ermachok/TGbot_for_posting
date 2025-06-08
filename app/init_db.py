from sqlalchemy.orm import Session

from app.database.database import Base, SessionLocal, engine
from app.models.post import Post
from app.models.user import User
from app.utils.security import hash_password


def init():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    if not db.query(User).filter_by(username="admin").first():
        user = User(username="admin", hashed_password=hash_password("admin123"))
        db.add(user)

        init_post = Post(title="initial test title", content="initial test content")
        db.add(init_post)

        db.commit()

        print("✅ Default user 'admin' created")
    else:
        print("ℹ️ Default user already exists")
    db.close()
