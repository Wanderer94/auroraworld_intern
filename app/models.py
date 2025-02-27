from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# SQLAlchemy의 Base 클래스 생성
Base = declarative_base()

# 사용자 테이블 (User)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # 사용자와 웹 링크 관계 (1:N)
    links = relationship("WebLink", back_populates="user")
    shared_links = relationship("SharedLink", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

# 웹 링크 테이블 (WebLink)
class WebLink(Base):
    __tablename__ = "web_links"

    id = Column(Integer, primary_key=True, index=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    url = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # 관계 설정
    user = relationship("User", back_populates="links")
    shared_users = relationship("SharedLink", back_populates="web_link")

    def __repr__(self):
        return f"<WebLink(id={self.id}, name={self.name}, created_by={self.created_by})>"

# 공유된 웹 링크 테이블 (SharedLink)
class SharedLink(Base):
    __tablename__ = "shared_links"

    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, ForeignKey("web_links.id"), nullable=False)
    shared_with = Column(Integer, ForeignKey("users.id"), nullable=False)
    permission = Column(String(10), nullable=False)  # 'read' 또는 'write'
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # 관계 설정
    web_link = relationship("WebLink", back_populates="shared_users")
    user = relationship("User", back_populates="shared_links")

    def __repr__(self):
        return f"<SharedLink(id={self.id}, link_id={self.link_id}, shared_with={self.shared_with}, permission={self.permission})>"
