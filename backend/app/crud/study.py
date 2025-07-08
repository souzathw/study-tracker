from sqlalchemy.orm import Session
from datetime import date, datetime
from sqlalchemy import func
from app.db.models.study_day import StudyDay
from app.db.models.study_block import StudyBlock
from app.db.models.tag import Tag
from app.schemas.study import TagCreate, StudyBlockCreate

def create_study_day(db: Session, user_id: int):
    today = date.today()
    day = db.query(StudyDay).filter_by(user_id=user_id, date=today).first()
    if not day:
        day = StudyDay(user_id=user_id, date=today)
        db.add(day)
        db.commit()
        db.refresh(day)
    return day

def create_tag(db: Session, user_id: int, tag_data: TagCreate):
    tag = Tag(name=tag_data.name, type=tag_data.type, user_id=user_id)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def create_study_block(db: Session, user_id: int, block_data: StudyBlockCreate):
    study_day = db.query(StudyDay).filter_by(id=block_data.study_day_id, user_id=user_id).first()
    if not study_day:
        raise ValueError("Dia de estudo não encontrado")
    block = StudyBlock(**block_data.dict())
    db.add(block)
    db.commit()
    db.refresh(block)
    return block

def get_dashboard_data(db: Session, user_id: int):
    today = date.today()
    start_week = today.fromisocalendar(today.isocalendar().year, today.isocalendar().week, 1)
    start_month = today.replace(day=1)

    def sum_blocks(start_date):
        result = (
            db.query(StudyBlock.type, func.sum(StudyBlock.duration_minutes))
            .join(StudyDay)
            .filter(StudyDay.user_id == user_id, StudyDay.date >= start_date)
            .group_by(StudyBlock.type)
            .all()
        )
        return [{"type": r[0], "minutes": r[1]} for r in result]

    def most_tags(start_date):
        result = (
            db.query(Tag.name, StudyBlock.type, func.count(StudyBlock.id).label("count"))
            .join(StudyBlock)
            .join(StudyDay)
            .filter(StudyDay.user_id == user_id, StudyDay.date >= start_date)
            .group_by(Tag.name, StudyBlock.type)
            .order_by(func.count(StudyBlock.id).desc())
            .limit(5)
            .all()
        )
        return [{"name": r[0], "type": r[1], "count": r[2]} for r in result]

    return {
        "day": sum_blocks(today),
        "week": sum_blocks(start_week),
        "month": sum_blocks(start_month),
        "top_tags": most_tags(start_month)
    }
