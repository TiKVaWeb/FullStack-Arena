from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime,
    JSON,
    Table,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func
from .db import Base

# Таблица для связи Many-to-Many между UserST и Dialog
dialog_participants = Table(
    "dialog_participants",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("dialog_id", Integer, ForeignKey("dialogs.id")),
)

class UserST(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True)
    registered_date = Column(DateTime, server_default=func.now())
    trade_link = Column(String, default="", nullable=True)
    count_buy = Column(Integer, default=0)
    count_sell = Column(Integer, default=0)
    rating = Column(Float, default=5.00)
    inventory_json = Column(JSON, default={})
    steam_ID = Column(String(17), unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    telegram = Column(String(20), unique=True, index=True, nullable=True)

    items = relationship("ItemST", back_populates="user")
    dialogs = relationship("Dialog", secondary=dialog_participants, back_populates="participants")
    sent_messages = relationship("Message", foreign_keys="Message.sender_id", back_populates="sender")
    received_messages = relationship("Message", foreign_keys="Message.receiver_id", back_populates="receiver")

    def __repr__(self):
        return f"<UserST(username={self.username}, steam_ID={self.steam_ID})>"

class ItemST(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    item_steam_ID = Column(String(25), unique=True, index=True, nullable=True)
    price = Column(Float)
    status_trade = Column(Boolean, default=True)
    date_push_item = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("UserST", back_populates="items")
    trades = relationship("TradeST", back_populates="item")

    def __repr__(self):
        return f"<ItemST(item_steam_ID={self.item_steam_ID})>"

class TradeST(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    trade_status_st = Column(
        ENUM("получен", "ожидает оплаты", "отменен", name="trade_status_enum"),
        default="ожидает оплаты",
    )
    item_id = Column(Integer, ForeignKey("items.id"))
    buyer_ID = Column(String(17), nullable=True)
    date_push_trade = Column(DateTime, server_default=func.now())

    item = relationship("ItemST", back_populates="trades")

    def __repr__(self):
        return f"<TradeST(item_id={self.item_id}, buyer_ID={self.buyer_ID})>"

class Dialog(Base):
    __tablename__ = "dialogs"
    id = Column(Integer, primary_key=True, index=True)
    last_message_id = Column(Integer, ForeignKey("messages.id"), nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    participants = relationship("UserST", secondary=dialog_participants, back_populates="dialogs")
    messages = relationship("Message", back_populates="dialog")
    last_message = relationship("Message", foreign_keys=[last_message_id])

    def __repr__(self):
        return f"<Dialog(id={self.id})>"

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    dialog_id = Column(Integer, ForeignKey("dialogs.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
    is_read = Column(Boolean, default=False)

    dialog = relationship("Dialog", back_populates="messages")
    sender = relationship("UserST", foreign_keys=[sender_id], back_populates="sent_messages")
    receiver = relationship("UserST", foreign_keys=[receiver_id], back_populates="received_messages")

    def __repr__(self):
        return f"<Message(sender_id={self.sender_id}, receiver_id={self.receiver_id})>"