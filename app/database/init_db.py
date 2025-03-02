import os
import sys

# 프로젝트 루트를 sys.path에 추가하여 모듈 인식 문제 해결
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import subprocess

from core.config import settings
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def initialize_database():
    """데이터베이스와 테이블을 자동 생성하는 함수"""
    print("📌 데이터베이스 초기화 중...")

    # 데이터베이스 엔진 생성
    engine = create_engine(settings.DATABASE_URL, echo=True)

    # 데이터베이스가 존재하지 않으면 생성
    with engine.connect() as conn:
        conn.execute("commit")  # 필요 시 커밋
        conn.execute(f"CREATE DATABASE fastapi_db;")  # DB 생성
        print("✅ 데이터베이스 생성 완료!")

    # Alembic 마이그레이션 실행
    print("📌 Alembic 마이그레이션 실행 중...")
    subprocess.run(["alembic", "upgrade", "head"])
    print("✅ Alembic 마이그레이션 완료!")


if __name__ == "__main__":
    initialize_database()
