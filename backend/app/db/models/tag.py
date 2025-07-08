from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.db.base import Base
import enum

class TagType(str, enum.Enum):
    study = "study"
    pause = "pause"

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(Enum(TagType), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
