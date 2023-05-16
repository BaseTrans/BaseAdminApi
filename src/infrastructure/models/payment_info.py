from datetime import datetime
from sqlalchemy.orm import backref

from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.databases import sqlalchemy_db as db
from .common.entity import UuidEntity, BaseEntity
from .model_extension import ModelExtension


class PaymentInfo(BaseEntity, UuidEntity, db.Model, ModelExtension):

    __tablename__ = 'PaymentInfo'

    account_id: UUID = db.Column(UUID(as_uuid=True), db.ForeignKey('Accounts.id'))
    charge_amount_per_month = db.Column(db.Float())
    last_pay_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_pay_amount = db.Column(db.Float())
    next_pay_date = db.Column(db.DateTime, default=datetime.utcnow)

