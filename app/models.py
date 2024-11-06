from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, unique=False, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.profile_id", ondelete="SET NULL"))
    
    # Establish a bidirectional relationship with Profile
    profile = relationship("Profile", back_populates="user", uselist=False, foreign_keys=[profile_id])

class Profile(Base):
    __tablename__ = "profiles"
    
    profile_id = Column(Integer, primary_key=True, index=True)
    bio = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    product = Column(String, index=True)

    # Establish a bidirectional relationship with User
    user = relationship("User", back_populates="profile", foreign_keys=[user_id])
