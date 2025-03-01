from pydantic import BaseModel
from datetime import datetime

# 공유 요청 데이터 모델
class SharedLinkCreate(BaseModel):
    shared_with: int  # 공유 대상 사용자 ID
    permission: str  # 'read' 또는 'write'

# 공유된 링크 응답 데이터 모델
class SharedLinkResponse(BaseModel):
    id: int
    link_id: int
    shared_with: int
    permission: str
    created_at: datetime

    class Config:
        orm_mode = True
