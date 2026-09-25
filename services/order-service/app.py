from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Order Service"
)


orders = {

    "10452": {
        "order_id": "10452",
        "customer_id": "7821",
        "status": "FAILED",
        "amount": 850.00,
        "currency": "EUR",
        "payment_id": "PAY-10452",
    },

    "12045": {
        "order_id": "12045",
        "customer_id": "9001",
        "status": "COMPLETED",
        "amount": 120.00,
        "currency": "EUR",
        "payment_id": "PAY-12045",
    },
}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/orders/{order_id}")
def get_order(order_id: str):

    order = orders.get(order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order