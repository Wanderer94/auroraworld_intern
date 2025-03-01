from sqlalchemy.orm import Session
from app.models.link import WebLink
from app.schemas.link import LinkCreate

def create_link(db: Session, link: LinkCreate, user_id: int):
    """새로운 웹 링크를 생성하는 함수"""
    db_link = WebLink(created_by=user_id, **link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def get_user_links(db: Session, user_id: int):
    """현재 로그인한 사용자의 웹 링크만 조회하는 함수"""
    return db.query(WebLink).filter(WebLink.created_by == user_id).all()

def get_link_by_id(db: Session, link_id: int):
    """특정 웹 링크를 조회하는 함수"""
    return db.query(WebLink).filter(WebLink.id == link_id).first()

def update_link(db: Session, link_id: int, link_data: LinkCreate):
    """웹 링크 정보를 수정하는 함수"""
    db_link = db.query(WebLink).filter(WebLink.id == link_id).first()
    if db_link:
        for key, value in link_data.dict().items():
            setattr(db_link, key, value)
        db.commit()
        db.refresh(db_link)
    return db_link

def delete_link(db: Session, link_id: int):
    """웹 링크 삭제 함수"""
    db_link = db.query(WebLink).filter(WebLink.id == link_id).first()
    if db_link:
        db.delete(db_link)
        db.commit()
        return True
    return False
