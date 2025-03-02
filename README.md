# auroraworld_intern

## 1. 프로젝트 개요

### 1.1 프로젝트명

웹 링크 관리 시스템

### 1.2 프로젝트 목표

사용자가 웹 링크를 관리하고, 카테고리별로 정리하며, 다른 사용자와 공유할 수 있도록 하는 시스템을 개발한다. JWT 인증을 사용하여 보안을 강화하며, 웹 애플리케이션의 기본적인 CRUD 기능을 제공한다.

### 1.3 주요 기능

- 회원가입 및 로그인 (JWT 인증)
- 웹 링크 추가, 수정, 삭제
- 웹 링크 공유 (읽기/쓰기 권한 설정)
- 웹 링크 검색 및 필터링
- 보안 및 접근 제어 (인증이 필요한 API 보호)
- Swagger(OpenAPI) 기반 API 문서 및 테스트 제공

---

## 2. 문서 관리

프로젝트의 상세한 설계 문서는 `docs/` 디렉토리에서 확인할 수 있습니다.

### 2.1 문서 구성

| 문서명                    | 설명                 |
| ------------------------- | -------------------- |
| `docs/architecture.md`    | 시스템 아키텍처 설계 |
| `docs/database_schema.md` | 데이터베이스 설계    |
| `docs/api_spec.md`        | API 명세서           |

---

## 3. 실행 방법

### 3.1 환경 설정 및 실행

```sh
# 프로젝트 클론
git clone https://github.com/Wanderer94/auroraworld_intern.git
cd link-management

# 가상 환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

# 종속성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload
```

### 3.2 API 문서 확인

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 3.3 데이터베이스 설정

이 프로젝트는 **PostgreSQL**을 사용합니다. 데이터베이스를 생성하려면 PostgreSQL을 설치한 후, `.env` 파일을 설정하고 아래 명령어를 실행하세요.

#### 1️⃣ `.env` 파일 설정

프로젝트 루트 디렉토리에 `.env` 파일을 만들고 아래 내용을 추가하세요.

```ini
DATABASE_URL=postgresql://fastapi_user:securepassword@localhost:5432/fastapi_db
```

#### 2️⃣ 명령어 입력

```sh
# 1️⃣ PostgreSQL에서 직접 데이터베이스 생성
psql -U postgres -c "CREATE DATABASE fastapi_db;"

# 2️⃣ .env 설정 확인
cat .env  # DATABASE_URL이 올바르게 설정되었는지 확인

# 3️⃣ Alembic 마이그레이션 실행
alembic upgrade head
```

---

## 4. 기술 스택

- **Backend:** FastAPI (Python 3.10+)
- **Database:** PostgreSQL
- **Authentication:** JWT (PyJWT)
- **API Documentation:** Swagger (FastAPI 내장)
