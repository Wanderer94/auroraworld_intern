from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.link import WebLink
from app.schemas.link import LinkCreate

def get_link_by_id(db: Session, link_id: int):
    """ID로 웹 링크를 조회하는 공통 함수"""
    db_link = db.query(WebLink).filter(WebLink.id == link_id).first()
    if not db_link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
    return db_link

def check_link_owner(db_link: WebLink, user_id: int):
    """현재 사용자가 해당 링크의 소유자인지 확인하는 함수"""
    if db_link.created_by != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to modify this link")

def create_link(db: Session, link: LinkCreate, user_id: int):
    """새로운 웹 링크를 생성하는 함수"""
    try:
        db_link = WebLink(created_by=user_id, **link.dict())
        db.add(db_link)
        db.commit()
        db.refresh(db_link)
        return db_link
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create link")

def get_user_links(db: Session, user_id: int):
    """현재 로그인한 사용자의 웹 링크만 조회하는 함수"""
    return db.query(WebLink).filter(WebLink.created_by == user_id).all()

def update_link(db: Session, link_id: int, link_data: LinkCreate, user_id: int):
    """웹 링크 수정 함수 (본인만 가능)"""
    db_link = get_link_by_id(db, link_id)  # 🔹 중복 제거 (공통 조회 함수 활용)
    check_link_owner(db_link, user_id)  # 🔹 소유권 검사 추가

    try:
        for key, value in link_data.dict().items():
            setattr(db_link, key, value)
        db.commit()
        db.refresh(db_link)
        return db_link
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update link")

def delete_link(db: Session, link_id: int, user_id: int):
    """웹 링크 삭제 함수 (본인만 가능)"""
    db_link = get_link_by_id(db, link_id)  # 🔹 중복 제거 (공통 조회 함수 활용)
    check_link_owner(db_link, user_id)  # 🔹 소유권 검사 추가

    try:
        db.delete(db_link)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete link")
