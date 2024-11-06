from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate, profile_id: int = None):
    db_user = models.User(name=user.name, email=user.email, profile_id=profile_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_profile(db: Session, profile: schemas.ProfileCreate, user_id: int = None):
    db_profile = models.Profile(bio=profile.bio, user_id=user_id)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.profile_id == profile_id).first()
