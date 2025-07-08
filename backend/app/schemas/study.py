from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class BlockType(str, Enum):
    study = "study"
    pause = "pause"

class TagCreate(BaseModel):
    name: str
    type: BlockType

class StudyBlockCreate(BaseModel):
    study_day_id: int
    tag_id: int
    start_time: datetime
    end_time: datetime
    duration_minutes: int
    type: BlockType
