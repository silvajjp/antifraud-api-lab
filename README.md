# AntiFraud API

Risk Analyst I - Case
This API evaluates credit card transactions and recommends approval or denial based on predefined antifraud rules. 

##  Features

- Denies transactions from users with previous chargebacks.
- Denies users with more than 3 transactions in the past hour.
- Denies transactions that exceed a daily total of 5000.0.

##  How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2- Run THe API:

uvicorn app.main:app --reload

3- Access the documentation:

http://localhost:8000/docs

## Endpoint

POST /evaluate

Payload example:

{
  "transaction_id": 123,
  "merchant_id": 456,
  "user_id": 789,
  "card_number": "123456******7890",
  "transaction_date": "2023-01-01T12:00:00",
  "transaction_amount": 100.0,
  "device_id": 321
}

Response example:

{
  "transaction_id": 123,
  "recommendation": "approve"
}
