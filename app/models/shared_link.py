from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class SharedLink(Base):
    __tablename__ = "shared_links"

    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, ForeignKey("web_links.id"), nullable=False)
    shared_with = Column(Integer, ForeignKey("users.id"), nullable=False)
    permission = Column(String(10), nullable=False)  # 'read' 또는 'write'
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    web_link = relationship("WebLink")
    user = relationship("User")
