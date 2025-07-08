from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.study import TagCreate, StudyBlockCreate
from app.crud import study as crud
from app.db.models.user import User

router = APIRouter()

@router.post("/start-day")
def start_study_day(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    return crud.create_study_day(db, current_user.id)

@router.post("/tag")
def create_tag(
    tag: TagCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    return crud.create_tag(db, current_user.id, tag)

@router.post("/block")
def create_study_block(
    block: StudyBlockCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    try:
        return crud.create_study_block(db, current_user.id, block)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/dashboard")
def get_dashboard(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    return crud.get_dashboard_data(db, current_user.id)
