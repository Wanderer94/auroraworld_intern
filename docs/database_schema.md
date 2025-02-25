# 데이터베이스 스키마 (Database Schema)

## 1. 개요

이 문서는 웹 링크 관리 시스템의 데이터베이스 구조를 설명합니다.  
이 시스템은 **PostgreSQL**을 사용하며, **SQLAlchemy ORM**을 활용하여 데이터 모델을 관리합니다.

---

## 2. ERD (Entity-Relationship Diagram)

### **📌 테이블 관계**

```
[users] 1 ─── N [web_links]
[users] 1 ─── N [shared_links]
[web_links] 1 ─── N [shared_links]
```

- `users` 테이블은 **웹 링크를 생성**할 수 있습니다.
- `web_links` 테이블은 **여러 사용자와 공유될 수 있으며**, `shared_links` 테이블에서 공유 정보를 관리합니다.

---

## 3. 테이블 정의

### **3.1 `users` (사용자 테이블)**

사용자 정보를 저장하는 테이블입니다.  
| 필드명 | 타입 | 설명 |
|------------|-----------------------------------|--------------------------|
| id | SERIAL PRIMARY KEY | 사용자 고유 ID (자동 증가) |
| username | VARCHAR(255) UNIQUE NOT NULL | 사용자 아이디 (고유) |
| password_hash | TEXT NOT NULL | 해싱된 비밀번호 |
| created_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 계정 생성일 |

📌 **제약조건**:

- `username`은 **중복될 수 없음(UNIQUE)**
- `password_hash`는 **보안을 위해 해싱된 형태로 저장**

---

### **3.2 `web_links` (웹 링크 테이블)**

사용자가 저장한 웹 링크를 관리하는 테이블입니다.  
| 필드명 | 타입 | 설명 |
|------------|-----------------------------------|--------------------------|
| id | SERIAL PRIMARY KEY | 웹 링크 고유 ID |
| created_by | INT NOT NULL, ForeignKey(users.id) | 생성한 사용자 ID |
| name | VARCHAR(255) NOT NULL | 웹 링크 이름 |
| url | TEXT NOT NULL | 저장할 웹사이트 URL |
| category | VARCHAR(100) NOT NULL | 카테고리 |
| created_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 등록 날짜 |

📌 **제약조건**:

- `created_by`는 **users 테이블을 참조 (ForeignKey)**
- `url`은 반드시 입력해야 함 (NOT NULL)

📌 **ForeignKey 관계**:

- `created_by` → `users.id` (웹 링크를 생성한 사용자)

---

### **3.3 `shared_links` (공유된 링크 테이블)**

웹 링크를 다른 사용자와 공유할 때 사용하는 테이블입니다.  
| 필드명 | 타입 | 설명 |
|------------|-----------------------------------|--------------------------|
| id | SERIAL PRIMARY KEY | 공유된 링크 고유 ID |
| link_id | INT NOT NULL, ForeignKey(web_links.id) | 공유된 웹 링크 ID |
| shared_with | INT NOT NULL, ForeignKey(users.id) | 공유 대상 사용자 ID |
| permission | VARCHAR(10) CHECK ('read', 'write') | 읽기/쓰기 권한 |
| created_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 공유 일시 |

📌 **제약조건**:

- `permission` 값은 `'read'` 또는 `'write'` 중 하나만 가능 (CHECK 제약조건)
- `shared_with`는 **users 테이블을 참조**

📌 **ForeignKey 관계**:

- `link_id` → `web_links.id` (공유된 웹 링크)
- `shared_with` → `users.id` (공유된 사용자)

---

## 4. 데이터베이스 설정 및 마이그레이션

### **4.1 환경 변수 설정**

`.env` 파일을 생성하여 데이터베이스 설정을 저장합니다.

📌 **`.env` 파일 예시**

```ini
DATABASE_URL=postgresql://fastapi_user:securepassword@localhost:5432/fastapi_db
```

---

### **4.2 데이터베이스 자동 생성**

터미널에서 아래 명령어를 실행하면, PostgreSQL에 **데이터베이스 및 테이블이 자동 생성**됩니다.

```sh
# 데이터베이스 및 테이블 생성
python app/init_db.py
```

📌 실행 결과 예시:

```sh
📌 데이터베이스 생성 중...
✅ 데이터베이스 및 테이블 생성 완료!
```

---

### **4.3 Alembic을 활용한 마이그레이션 관리**

데이터베이스 스키마가 변경될 경우 **Alembic을 사용하여 마이그레이션을 적용**할 수 있습니다.

📌 **Alembic 초기화**

```sh
alembic init alembic
```

📌 **데이터베이스 URL 설정 (alembic.ini 수정)**

```ini
sqlalchemy.url = postgresql://fastapi_user:securepassword@localhost:5432/fastapi_db
```

📌 **마이그레이션 파일 생성 및 적용**

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## 5. ERD 다이어그램

(추후 ERD 이미지 삽입 가능)

---
