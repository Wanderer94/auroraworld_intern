# API 명세서

## 1. 개요

본 문서는 웹 링크 관리 시스템의 RESTful API를 정의합니다. FastAPI를 기반으로 구축되었으며, 인증에는 JWT(JSON Web Token)를 사용합니다.

## 2. 인증 및 보안

- 모든 보호된 API는 **JWT 인증 토큰**이 필요합니다.
- 인증 헤더 예시:
  ```http
  Authorization: Bearer <JWT_TOKEN>
  ```

## 3. API 엔드포인트 명세

### **3.1 사용자 인증 API**

| 메서드 | 엔드포인트 | 설명                                |
| ------ | ---------- | ----------------------------------- |
| POST   | /register  | 사용자 회원가입                     |
| POST   | /login     | 로그인 및 JWT 토큰 발급             |
| POST   | /logout    | 로그아웃 (클라이언트에서 토큰 삭제) |

#### **회원가입 (POST /register)**

**요청 예시**

```json
{
  "username": "testuser",
  "password": "securepassword"
}
```

**응답 예시**

```json
{
  "id": 1,
  "username": "testuser"
}
```

### **3.2 웹 링크 관리 API**

| 메서드 | 엔드포인트  | 설명              |
| ------ | ----------- | ----------------- |
| POST   | /links      | 웹 링크 추가      |
| PUT    | /links/{id} | 웹 링크 수정      |
| DELETE | /links/{id} | 웹 링크 삭제      |
| GET    | /links      | 웹 링크 목록 조회 |

#### **웹 링크 추가 (POST /links)**

**요청 예시**

```json
{
  "name": "React Docs",
  "url": "https://reactjs.org",
  "category": "교육"
}
```

**응답 예시**

```json
{
  "id": 10,
  "name": "React Docs",
  "url": "https://reactjs.org",
  "category": "교육",
  "created_by": 1
}
```

### **3.3 공유 API**

| 메서드 | 엔드포인트        | 설명                    |
| ------ | ----------------- | ----------------------- |
| POST   | /links/{id}/share | 특정 사용자와 링크 공유 |
| GET    | /links/shared     | 공유된 링크 조회        |

#### **링크 공유 (POST /links/{id}/share)**

**요청 예시**

```json
{
  "shared_with": 2,
  "permission": "write"
}
```

**응답 예시**

```json
{
  "id": 5,
  "link_id": 10,
  "shared_with": 2,
  "permission": "write"
}
```

### **3.4 검색 및 필터 API**

| 메서드 | 엔드포인트           | 설명              |
| ------ | -------------------- | ----------------- |
| GET    | /links?search=react  | 키워드 검색       |
| GET    | /links?category=교육 | 카테고리별 필터링 |

#### **키워드 검색 (GET /links?search=react)**

**응답 예시**

```json
[
  {
    "id": 10,
    "name": "React Docs",
    "url": "https://reactjs.org",
    "category": "교육"
  }
]
```

## 4. 에러 응답 형식

모든 API 요청이 실패하면 **HTTP 상태 코드**와 함께 표준 오류 응답을 반환합니다.

**예시:**

```json
{
  "detail": "잘못된 요청입니다."
}
```

## 5. 결론

본 문서는 웹 링크 관리 시스템의 API 엔드포인트를 정의하며, JWT 인증, CRUD 작업, 공유 기능 및 검색 기능을 포함합니다.
