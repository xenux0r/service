import typing as t
from service.api.models.base import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func
from sqlalchemy.engine.row import Row


class Request(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    value_name = db.Column(db.String(80))
    groups = db.Column(JSON)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
