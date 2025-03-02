from pydantic import BaseModel, EmailStr
from datetime import datetime


# 회원가입 요청 데이터 모델
class UserCreate(BaseModel):
    username: str
    password: str


# 회원 응답 데이터 모델
class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


# 로그인 요청 데이터 모델
class UserLogin(BaseModel):
    username: str
    password: str
