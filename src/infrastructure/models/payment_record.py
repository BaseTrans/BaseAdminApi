from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref

from src.infrastructure.databases import sqlalchemy_db as db
from .common.entity import IntEntity, BaseEntity
from .model_extension import ModelExtension


class PaymentRecord(BaseEntity, IntEntity, db.Model, ModelExtension):

    __tablename__ = 'PaymentRecords'

    transaction_id = db.Column(db.Integer, db.ForeignKey('BankRecords.id'))
    account_id: UUID = db.Column(UUID(as_uuid=True), db.ForeignKey('Accounts.id'))
