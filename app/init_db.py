import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base  # 데이터베이스 모델 불러오기
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """데이터베이스 및 테이블 자동 생성"""
    print("📌 데이터베이스 생성 중...")
    Base.metadata.create_all(bind=engine)
    print("✅ 데이터베이스 및 테이블 생성 완료!")

if __name__ == "__main__":
    init_db()