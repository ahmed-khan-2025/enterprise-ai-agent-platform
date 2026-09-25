import httpx

from app.config import settings


def get_logs(order_id: str) -> dict:

    response = httpx.get(
        f"{settings.logging_service_url}/logs/{order_id}",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()