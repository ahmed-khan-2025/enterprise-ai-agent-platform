from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Payment Service"
)


payments = {

    "10452": {
        "payment_id": "PAY-10452",
        "order_id": "10452",
        "status": "DECLINED",
        "error_code": "PAYMENT_402",
        "attempts": 3,
    },

    "12045": {
        "payment_id": "PAY-12045",
        "order_id": "12045",
        "status": "APPROVED",
        "error_code": None,
        "attempts": 1,
    },
}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/payments/{order_id}")
def get_payment(order_id: str):

    payment = payments.get(order_id)

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found",
        )

    return payment