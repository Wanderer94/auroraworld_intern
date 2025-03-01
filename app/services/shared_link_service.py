from sqlalchemy.orm import Session
from app.models.shared_link import SharedLink
from app.schemas.shared_link import SharedLinkCreate

def share_link(db: Session, link_id: int, shared_data: SharedLinkCreate):
    """웹 링크를 특정 사용자와 공유하는 함수"""
    shared_link = SharedLink(link_id=link_id, **shared_data.dict())
    db.add(shared_link)
    db.commit()
    db.refresh(shared_link)
    return shared_link

def get_shared_links(db: Session, user_id: int):
    """현재 사용자가 공유받은 웹 링크 목록을 조회하는 함수"""
    return db.query(SharedLink).filter(SharedLink.shared_with == user_id).all()
