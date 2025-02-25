# 시스템 아키텍처 설계

## 1. 개요

웹 링크 관리 시스템은 FastAPI를 기반으로 구축되며, PostgreSQL을 데이터 저장소로 사용합니다. JWT를 활용한 인증 시스템을 도입하여 보안을 강화하며, API 문서는 Swagger(OpenAPI)를 통해 제공됩니다.

## 2. 전체 시스템 구성도

다음은 시스템의 주요 구성 요소와 데이터 흐름을 설명하는 아키텍처 다이어그램입니다.

```
[Frontend (Optional)] → [FastAPI Backend] → [PostgreSQL Database]
                            ↓
                    [JWT Authentication]
                            ↓
              [Swagger (API Documentation)]
```

### **2.1 주요 구성 요소**

- **FastAPI**: 백엔드 프레임워크로 사용하여 API 서버를 구축.
- **PostgreSQL**: 관계형 데이터베이스, 트랜잭션 지원 및 확장성 고려.
- **JWT (JSON Web Token)**: 사용자 인증 및 권한 부여.
- **Swagger (OpenAPI Docs)**: API 문서 제공 및 테스트 가능.
- **Docker (Optional)**: 컨테이너화를 통한 배포 환경 구축 가능.

## 3. 데이터 흐름

### **3.1 사용자 인증 흐름**

1. 사용자가 회원가입(/register) 또는 로그인(/login) 요청을 보냄.
2. FastAPI 서버는 사용자의 입력값을 검증 후, JWT 토큰을 발급.
3. 이후 사용자는 보호된 API 요청 시 `Authorization: Bearer <JWT>` 헤더를 포함하여 요청.
4. 서버는 JWT를 검증 후, 요청을 처리하여 데이터를 반환.

### **3.2 웹 링크 관리 흐름**

1. 사용자는 새로운 웹 링크를 추가(/links) 요청.
2. 서버는 `created_by` 필드와 함께 PostgreSQL에 링크 데이터를 저장.
3. 사용자는 자신이 등록한 링크를 수정(/links/{id}) 또는 삭제(/links/{id}) 가능.
4. 링크 검색(/links?search=react) 및 카테고리 필터링 기능 제공.

### **3.3 공유 및 권한 관리 흐름**

1. 사용자가 웹 링크를 특정 사용자에게 공유(/links/{id}/share) 요청.
2. 서버는 `shared_links` 테이블을 통해 공유 권한을 저장.
3. 공유된 사용자는 링크를 조회(/links/shared) 가능하며, 쓰기 권한이 있을 경우 수정 가능.

## 4. 보안 및 성능 고려 사항

### **4.1 보안**

- 비밀번호는 `bcrypt`를 사용하여 해싱 후 저장.
- 모든 API 요청에 JWT 인증 적용하여 보안 강화.
- SQL Injection, XSS, CSRF 방지를 위한 보안 정책 적용.

### **4.2 성능 최적화**

- DB Indexing을 활용하여 검색 속도 향상.
- FastAPI의 비동기(async) 지원을 활용하여 높은 동시 요청 처리.
- Redis 또는 캐시 시스템 적용 가능성 검토.

## 5. 결론

이 문서는 웹 링크 관리 시스템의 전체적인 아키텍처를 정의하며, 주요 구성 요소 및 데이터 흐름을 설명합니다. 추가적인 확장 기능(소셜 로그인, 태그 기반 검색 등)은 향후 고려될 수 있습니다.
