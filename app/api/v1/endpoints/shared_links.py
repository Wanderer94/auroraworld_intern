from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.session import get_db
from app.schemas.shared_link import SharedLinkCreate, SharedLinkResponse
from app.services.shared_link_service import get_shared_links, share_link

router = APIRouter()


@router.post("/{link_id}/share", response_model=SharedLinkResponse)
def share_web_link(
    link_id: int, shared_data: SharedLinkCreate, db: Session = Depends(get_db)
):
    """웹 링크 공유 API"""
    return share_link(db=db, link_id=link_id, shared_data=shared_data)


@router.get("/shared", response_model=list[SharedLinkResponse])
def get_user_shared_links(
    db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """현재 로그인한 사용자가 공유받은 웹 링크 목록 조회 API"""
    return get_shared_links(db=db, user_id=current_user.id)
