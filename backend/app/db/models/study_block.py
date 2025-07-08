from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
import enum

class BlockType(str, enum.Enum):
    study = "study"
    pause = "pause"

class StudyBlock(Base):
    __tablename__ = "study_blocks"

    id = Column(Integer, primary_key=True, index=True)
    study_day_id = Column(Integer, ForeignKey("study_days.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    type = Column(Enum(BlockType), nullable=False)

    study_day = relationship("StudyDay", backref="blocks")
    tag = relationship("Tag")
