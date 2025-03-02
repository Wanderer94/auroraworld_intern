import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.session import get_db
from app.main import app
from app.models.base import Base  # 모든 모델의 부모 클래스 (테이블 생성용)

# ✅ **테스트용 SQLite 파일 기반 데이터베이스**
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ✅ **테스트용 DB 세션 설정**
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """테스트 실행 전에 테이블을 생성하고, 테스트 종료 후 삭제"""
    Base.metadata.create_all(bind=engine)  # ✅ 테이블 생성
    yield  # 테스트 실행
    Base.metadata.drop_all(bind=engine)  # ✅ 테스트 후 테이블 삭제


# ✅ FastAPI 앱에 테스트 DB 주입
app.dependency_overrides[get_db] = override_get_db

# ✅ 테스트 클라이언트 생성
client = TestClient(app)
