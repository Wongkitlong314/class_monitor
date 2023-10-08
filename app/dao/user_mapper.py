from sqlalchemy.orm import Session
from app.models import user
from app.config.database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError

class UserDAO:

    @staticmethod
    def get_all_users(db: Session = SessionLocal()):
        return db.query(user.User).all()

    # 更多的CRUD方法...