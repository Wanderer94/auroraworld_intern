from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.link import LinkCreate, LinkResponse
from app.models.link import WebLink
from app.services.link_service import (
    create_link,
    get_user_links,
    get_link_by_id,
    update_link,
    delete_link,
)
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=LinkResponse)
def create_new_link(
    link: LinkCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """웹 링크 생성 API (로그인 필수)"""
    return create_link(db=db, link=link, user_id=current_user.id)


@router.get("/", response_model=list[LinkResponse])
def get_links(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """현재 로그인한 사용자가 생성한 웹 링크 조회 API"""
    return get_user_links(db=db, user_id=current_user.id)


@router.get("/{link_id}", response_model=LinkResponse)
def get_link(
    link_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """특정 웹 링크 조회 API (본인만 가능)"""
    db_link = get_link_by_id(db=db, link_id=link_id)
    if not db_link or db_link.created_by != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this link",
        )
    return db_link


@router.put("/{link_id}", response_model=LinkResponse)
def update_link_data(
    link_id: int,
    link: LinkCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """웹 링크 수정 API (본인만 가능)"""
    db_link = get_link_by_id(db=db, link_id=link_id)
    if not db_link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Link not found"
        )
    if db_link.created_by != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this link",
        )

    return update_link(db=db, link_id=link_id, link_data=link)


@router.delete("/{link_id}")
def delete_link_data(
    link_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """웹 링크 삭제 API (본인만 가능)"""
    db_link = get_link_by_id(db=db, link_id=link_id)
    if not db_link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Link not found"
        )
    if db_link.created_by != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this link",
        )

    delete_link(db=db, link_id=link_id)
    return {"message": "Link deleted successfully"}
