from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

# SQLAlchemy의 Base 클래스 생성
Base = declarative_base()
