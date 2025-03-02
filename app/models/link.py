from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base


class WebLink(Base):
    __tablename__ = "web_links"

    id = Column(Integer, primary_key=True, index=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    url = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship("User")
