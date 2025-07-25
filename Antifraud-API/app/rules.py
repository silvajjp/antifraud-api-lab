from datetime import timedelta

MAX_TRANSACTIONS_PER_HOUR = 3
MAX_DAILY_AMOUNT = 5000.0

def evaluate(tx, user_tx, chargeback_users):
    if tx.user_id in chargeback_users:
        return "deny"
    
    tx_date = tx.transaction_date
    if tx_date.tzinfo is not None:
        tx_date = tx_date.tz_localize(None) if hasattr(tx_date, 'tz_localize') else tx_date.replace(tzinfo=None)
    
    one_hour_ago = tx_date - timedelta(hours=1)

    if user_tx["transaction_date"].dt.tz is not None:
        user_tx["transaction_date"] = user_tx["transaction_date"].dt.tz_localize(None)

    recent_tx = user_tx[
        (user_tx["transaction_date"] >= one_hour_ago) &
        (user_tx["transaction_date"] < tx_date)
    ]
    if len(recent_tx) >= MAX_TRANSACTIONS_PER_HOUR:
        return "deny"

    tx_day = tx_date.date()
    daily_total = user_tx[user_tx['transaction_date'].dt.date == tx_day]["transaction_amount"].sum()
    if daily_total + tx.transaction_amount > MAX_DAILY_AMOUNT:
        return "deny"
    
    return "approve"
