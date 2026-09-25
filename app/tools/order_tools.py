import httpx

from app.config import settings


def get_order(order_id: str) -> dict:

    response = httpx.get(
        f"{settings.order_service_url}/orders/{order_id}",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()