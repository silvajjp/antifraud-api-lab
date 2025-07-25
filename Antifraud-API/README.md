# AntiFraud API

This API evalutes credit card transaction and recommends approval or denial based on antifraud rules

## Features

- Deny Transactions from users with previous chargebacks.
- Deny users with more than 3 transactions in the past hour.
- Deny Transactions that exceed a daily total of 5000.0

## How to Run

1. Install dependencies:
    pip install -r requerements.txt

2. Run the API:
    uvicorn app.main:app --reload

3. Access the documantation:
    http://localhost:8000/docs

## Endpoints

POST / evaluete

Payload:
{
    "trasaction_id":123,
    "meerchant_id":456,
    "user_id":789,
    "card_number0":"123456******7890"
    "transaction_date:2023-01-01T12:00:00,
    "transaction_amount":100.0,
    "device_id":321
}

Responte:
{
    "transaction_id": 123,
    "recommendation": "approve"
}
