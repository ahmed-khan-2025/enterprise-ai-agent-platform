import httpx

from app.config import settings


def get_payment(order_id: str) -> dict:

    response = httpx.get(
        f"{settings.payment_service_url}/payments/{order_id}",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()