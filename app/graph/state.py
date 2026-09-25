from typing import TypedDict


class AgentState(TypedDict, total=False):

    user_query: str

    intent: str

    order_id: str

    customer_id: str

    order_data: dict

    customer_data: dict

    payment_data: dict

    logs: list[str]

    documents: list[str]

    diagnosis: str

    recommendation: str

    requires_human: bool

    final_response: str