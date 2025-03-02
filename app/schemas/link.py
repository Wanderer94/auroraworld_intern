from pydantic import BaseModel, HttpUrl
from datetime import datetime


# 웹 링크 생성 요청 데이터 모델
class LinkCreate(BaseModel):
    name: str
    url: HttpUrl
    category: str


# 웹 링크 응답 데이터 모델
class LinkResponse(BaseModel):
    id: int
    name: str
    url: str
    category: str
    created_at: datetime

    class Config:
        orm_mode = True
