from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# SQLAlchemy의 Base 클래스 생성
Base = declarative_base()
