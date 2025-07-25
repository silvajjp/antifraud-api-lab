from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.models import Transaction, Recommendation
from app.data_loader import load_data
from app.rules import evaluate

app = FastAPI()
data = load_data()
chargeback_users = set(data[data["has_cbk"]]["user_id"])

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.post("/evaluate", response_model=Recommendation)
def evalute_transaction(tx: Transaction):
    user_tx = data[data["user_id"] == tx.user_id]
    recommendation = evaluate(tx,user_tx,chargeback_users)
    return{"transaction_id":tx.transaction_id, "recommendation":recommendation}