from src.infrastructure.databases import sqlalchemy_db as db
from src.infrastructure.models.model_extension import ModelExtension
from sqlalchemy.orm import backref

from .common.entity import UuidEntity, BaseEntity
from .payment_record import PaymentRecord


class Account(BaseEntity, UuidEntity, db.Model, ModelExtension):

    __tablename__ = 'Accounts'

    name = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    door_id = db.Column(db.Integer())
    cabinet_num = db.Column(db.String())

    db_account_payment_records = db.relationship("PaymentRecord", backref="Accounts")
    db_account_payment_info = db.relationship("PaymentInfo", backref="Accounts")
