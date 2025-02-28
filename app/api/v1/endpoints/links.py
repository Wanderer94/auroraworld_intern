from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.link import LinkCreate, LinkResponse
from app.services.link_service import create_link, get_all_links, get_link_by_id, update_link, delete_link

router = APIRouter()

@router.post("/", response_model=LinkResponse)
def create_new_link(link: LinkCreate, db: Session = Depends(get_db)):
    """새로운 웹 링크 생성 API"""
    return create_link(db=db, link=link, user_id=1)  # 현재 user_id=1로 고정 (JWT 인증 추가 예정)

@router.get("/", response_model=list[LinkResponse])
def get_links(db: Session = Depends(get_db)):
    """모든 웹 링크 조회 API"""
    return get_all_links(db=db)

@router.get("/{link_id}", response_model=LinkResponse)
def get_link(link_id: int, db: Session = Depends(get_db)):
    """특정 웹 링크 조회 API"""
    db_link = get_link_by_id(db=db, link_id=link_id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link

@router.put("/{link_id}", response_model=LinkResponse)
def update_link_data(link_id: int, link: LinkCreate, db: Session = Depends(get_db)):
    """웹 링크 수정 API"""
    db_link = update_link(db=db, link_id=link_id, link_data=link)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link

@router.delete("/{link_id}")
def delete_link_data(link_id: int, db: Session = Depends(get_db)):
    """웹 링크 삭제 API"""
    if not delete_link(db=db, link_id=link_id):
        raise HTTPException(status_code=404, detail="Link not found")
    return {"message": "Link deleted successfully"}
