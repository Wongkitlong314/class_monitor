from sqlalchemy.orm import Session
from app.models.user import User
from app.config.database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError


class UserDAO:

    @staticmethod
    def get_all_users(db: Session = SessionLocal()):
        return db.query(User).all()

    # 更多的CRUD方法...
    @staticmethod
    def get_one_user(db: Session = SessionLocal(), id: int = 1):
        return db.query(User).filter(User.id == id).all()

    @staticmethod
    def get_user_by_phone(db: Session = SessionLocal(), phone: str = None):
        if not phone:
            return None

        # sql = "SELECT * FROM user where phone = :phone"
        print("phone={}".format(phone))
        result = db.query(User).filter(User.phone==phone)[0].name
        # result =db.query(User).all()[0].name
        return result
