from fastapi import FastAPI
from app.api.v1.api_router import api_router

app = FastAPI(title="FastAPI Web Link Manager")

# API 라우트 추가
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Web Link Manager!"}
