from src.infrastructure.databases import sqlalchemy_db as db
from sqlalchemy.orm import backref
from .common.entity import IntEntity, BaseEntity
from .model_extension import ModelExtension


class BankRecord(BaseEntity, IntEntity, db.Model, ModelExtension):

    __tablename__ = 'BankRecords'

    transaction_date = db.Column(db.DateTime, nullable=False)
    account_date = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.String)
    transaction_amount = db.Column(db.Numeric, nullable=False)
    balance = db.Column(db.Numeric, nullable=False)
    remark = db.Column(db.String)
    r_with_payment_records = db.relationship("PaymentRecord", backref=backref("BankRecords", uselist=False))
