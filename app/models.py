import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime,JSON
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True, index=True)
    password = Column(String(100))


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    subscribed_id = Column(Integer, ForeignKey("users.id"))
    feed_url = Column(String(100))


class FeedItem(Base):
    __tablename__ = "feed items"
    id = Column(Integer, primary_key=True, index=True)
    feed_obj = Column(JSON)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    read = Column(Boolean)
