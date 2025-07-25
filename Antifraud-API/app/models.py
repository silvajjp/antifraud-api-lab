from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class Transaction(BaseModel):
    transaction_id: int
    merchant_id: int
    user_id: int
    card_number: str
    transaction_date: datetime
    transaction_amount: float
    device_id: int

class Recommendation(BaseModel):
    transaction_id: int
    recommendation: Literal["approve", "deny"]