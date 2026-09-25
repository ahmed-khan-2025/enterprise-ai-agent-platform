import httpx

from app.config import settings


def get_customer(customer_id: str) -> dict:

    response = httpx.get(
        f"{settings.customer_service_url}/customers/{customer_id}",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()