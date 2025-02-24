# auroraworld_intern

# 1. 프로젝트 개요

## 1.1 프로젝트명

웹 링크 관리 시스템

## 1.2 프로젝트 목표

사용자가 웹 링크를 관리하고, 카테고리별로 정리하며, 다른 사용자와 공유할 수 있도록 하는 시스템을 개발한다. JWT 인증을 사용하여 보안을 강화하며, 웹 애플리케이션의 기본적인 CRUD 기능을 제공한다.

## 1.3 주요 기능

- 회원가입 및 로그인 (JWT 인증)
- 웹 링크 추가, 수정, 삭제
- 웹 링크 공유 (읽기/쓰기 권한 설정)
- 웹 링크 검색 및 필터링
- 보안 및 접근 제어 (인증이 필요한 API 보호)

---

# 2. 사용자 스토리

## 2.1 일반 사용자

- 아이디와 비밀번호로 회원가입을 하고 싶다.
  - 회원가입시 입력한 아이디가 중복되지 않는지 검사한다.
- 로그인하여 내 계정으로 웹 링크를 관리하고 싶다.
- 새로운 웹 링크를 추가하고, 필요한 경우 수정 및 삭제할 수 있다.
- 웹 링크를 카테고리별로 정리하고 싶다.
- 특정 웹 링크를 다른 사용자와 공유하고, 읽기 또는 쓰기 권한을 설정하고 싶다.
- 저장한 웹 링크를 키워드 검색과 카테고리별 필터링을 통해 쉽게 찾고 싶다.

## 2.2 공유 대상 사용자

- 다른 사용자가 공유한 웹 링크를 확인할 수 있다.
- 내가 읽기 권한만 있는 링크는 볼 수 있지만 수정할 수 없다.
- 내가 쓰기 권한이 있는 링크는 내용을 수정할 수 있다.

## 2.3 관리자 (Admin)

- 부적절한 콘텐츠가 있는 경우 사용자 계정을 차단할 수 있다. (향후 확장 기능)

---

# 3. 기능 명세

## 3.1 사용자 인증

| 기능     | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| 회원가입 | 사용자는 아이디와 비밀번호를 입력하여 계정을 생성할 수 있다. |
| 로그인   | JWT 기반 로그인 기능 제공                                    |
| 로그아웃 | JWT 토큰을 만료시켜 세션을 종료                              |

## 3.2 웹 링크 관리

| 기능         | 설명                                                                        |
| ------------ | --------------------------------------------------------------------------- |
| 웹 링크 추가 | 사용자는 새로운 웹 링크를 추가할 수 있다.                                   |
| 웹 링크 수정 | 사용자는 자신이 등록한 웹 링크 또는 쓰기 권한이 있는 링크를 수정할 수 있다. |
| 웹 링크 삭제 | 사용자는 자신이 등록한 웹 링크를 삭제할 수 있다.                            |

## 3.3 웹 링크 공유

| 기능           | 설명                                                   |
| -------------- | ------------------------------------------------------ |
| 웹 링크 공유   | 사용자는 특정 사용자와 웹 링크를 공유할 수 있다.       |
| 읽기 권한 설정 | 공유된 사용자는 웹 링크를 볼 수 있지만 수정할 수 없다. |
| 쓰기 권한 설정 | 공유된 사용자는 웹 링크를 수정할 수 있다.              |

## 3.4 검색 및 필터링

| 기능            | 설명                                        |
| --------------- | ------------------------------------------- |
| 키워드 검색     | 웹 링크 이름으로 검색 가능 (부분 일치 검색) |
| 카테고리 필터링 | 카테고리별로 웹 링크를 필터링               |

## 3.5 보안 및 접근 제어

| 기능                   | 설명                                                        |
| ---------------------- | ----------------------------------------------------------- |
| 인증이 필요한 API 보호 | 로그인하지 않은 사용자는 웹 링크 관련 API를 사용할 수 없다. |
| 인가 처리              | JWT 토큰을 이용하여 API 요청 권한을 확인                    |

---

# 4. 비기능 요구사항

## 4.1 성능

- 1초 이내에 검색 결과를 반환해야 한다.
- 100만 개 이상의 웹 링크 데이터를 처리할 수 있도록 설계한다.

## 4.2 보안

- 비밀번호는 해싱하여 저장 (예: bcrypt 사용)
- JWT 토큰 기반 인증 방식 사용
- SQL Injection, CSRF, XSS 방지

## 4.3 확장성

- 향후 태그 기반 검색 기능을 추가할 수 있도록 고려
- OAuth 기반 소셜 로그인 기능 확장 가능하도록 설계

---

# 5. 데이터 모델 정의

## 5.1 사용자 테이블 (`users`)

| 필드          | 타입                                | 설명            |
| ------------- | ----------------------------------- | --------------- |
| id            | SERIAL PRIMARY KEY                  | 사용자 고유 ID  |
| username      | VARCHAR(255) UNIQUE NOT NULL        | 사용자 이름     |
| password_hash | TEXT NOT NULL                       | 해싱된 비밀번호 |
| created_at    | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 생성 날짜       |

## 5.2 웹 링크 테이블 (`web_links`)

| 필드       | 타입                                | 설명             |
| ---------- | ----------------------------------- | ---------------- |
| id         | SERIAL PRIMARY KEY                  | 웹 링크 고유 ID  |
| created_by | INT NOT NULL                        | 생성한 사용자 ID |
| name       | VARCHAR(255) NOT NULL               | 웹 링크 이름     |
| url        | TEXT NOT NULL                       | 저장할 URL       |
| category   | VARCHAR(100) NOT NULL               | 카테고리         |
| created_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 생성 날짜        |

## 5.3 공유 테이블 (`shared_links`)

| 필드        | 타입                                | 설명                |
| ----------- | ----------------------------------- | ------------------- |
| id          | SERIAL PRIMARY KEY                  | 공유 고유 ID        |
| link_id     | INT NOT NULL                        | 공유된 웹 링크 ID   |
| shared_with | INT NOT NULL                        | 공유 대상 사용자 ID |
| permission  | VARCHAR(10) CHECK ('read', 'write') | 읽기/쓰기 권한      |
| created_at  | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | 생성 날짜           |

---

# 6. API 명세

## 6.1 사용자 인증 API

| 메서드 | 엔드포인트 | 설명              |
| ------ | ---------- | ----------------- |
| POST   | /register  | 회원가입          |
| POST   | /login     | 로그인 (JWT 발급) |
| POST   | /logout    | 로그아웃          |

## 6.2 웹 링크 API

| 메서드 | 엔드포인트  | 설명              |
| ------ | ----------- | ----------------- |
| POST   | /links      | 웹 링크 추가      |
| PUT    | /links/{id} | 웹 링크 수정      |
| DELETE | /links/{id} | 웹 링크 삭제      |
| GET    | /links      | 웹 링크 목록 조회 |

## 6.3 공유 API

| 메서드 | 엔드포인트        | 설명             |
| ------ | ----------------- | ---------------- |
| POST   | /links/{id}/share | 링크 공유        |
| GET    | /links/shared     | 공유된 링크 조회 |

## 6.4 검색 및 필터 API

| 메서드 | 엔드포인트           | 설명              |
| ------ | -------------------- | ----------------- |
| GET    | /links?search=react  | 키워드 검색       |
| GET    | /links?category=교육 | 카테고리별 필터링 |

---
