from fastapi import FastAPI


app = FastAPI(
    title="Logging Service"
)


logs = {

    "10452": [
        "Order created",
        "Payment authorization started",
        "Payment authorization failed",
        "Payment authorization retry 1 failed",
        "Payment authorization retry 2 failed",
        "Payment authorization retry 3 failed",
        "Order marked as FAILED",
    ],

    "12045": [
        "Order created",
        "Payment authorization started",
        "Payment approved",
        "Order completed",
    ],
}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/logs/{order_id}")
def get_logs(order_id: str):

    return {
        "order_id": order_id,
        "logs": logs.get(order_id, []),
    }