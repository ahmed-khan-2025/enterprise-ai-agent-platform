from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Customer Service"
)


customers = {

    "7821": {
        "customer_id": "7821",
        "name": "Anna Andersson",
        "status": "ACTIVE",
        "country": "Sweden",
    },

    "9001": {
        "customer_id": "9001",
        "name": "John Smith",
        "status": "ACTIVE",
        "country": "Sweden",
    },
}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):

    customer = customers.get(customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer