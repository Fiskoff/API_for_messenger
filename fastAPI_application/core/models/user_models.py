from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base_model import BaseModel


class UserProfile(BaseModel):
    __tablename__ = "User_profile"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    local_auth: Mapped[Optional["UserLocalAuth"]] = relationship(
        "UserLocalAuth",
        back_populates="profile",
        cascade="all, delete-orphan",
        uselist=False
    )
    oauth_providers: Mapped[List["UserOAuth"]] = relationship(
        "UserOAuth",
        back_populates="profile",
        cascade="all, delete-orphan"
    )


class UserLocalAuth(BaseModel):
    __tablename__ = "User_local_auth"

    user_id: Mapped[int] = mapped_column(ForeignKey("User_profile.id", ondelete="CASCADE"), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    refresh_token_hash: Mapped[Optional[str]] = mapped_column(String(525), nullable=True)

    profile: Mapped["UserProfile"] = relationship(
        "UserProfile",
        back_populates="local_auth"
    )


class UserOAuth(BaseModel):
    __tablename__ = "User_oauth"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User_profile.id", ondelete="CASCADE"))
    provider: Mapped[str] = mapped_column(String(20))
    provider_id: Mapped[str] = mapped_column(String(255))
    access_token: Mapped[str] = mapped_column(String(512))
    token_expiry: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    refresh_token: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)

    profile: Mapped["UserProfile"] = relationship(
        "UserProfile",
        back_populates="oauth_providers"
)