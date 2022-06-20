from email.policy import default
from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.sql import func
import datetime

from .base_class import Base


class PNUItem(Base):

    id = Column(Integer, primary_key=True, index=True)
    pnu = Column(String)
    program = Column(String)
    error_desc = Column(JSON)
    result = Column(JSON)
    is_error = Column(Boolean, default=False)
    is_fix = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now())
