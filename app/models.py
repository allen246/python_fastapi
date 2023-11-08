import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, Integer, LargeBinary, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

metadata = Base.metadata

class Profile(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    data = Column(LargeBinary)

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default='False')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    profile_id = Column(
        Integer, ForeignKey(Profile.id, ondelete="SET NULL"), nullable=True
    )
    profile = relationship(Profile, primaryjoin=profile_id == Profile.id)