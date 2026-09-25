from app.tools.order_tools import get_order
from app.tools.customer_tools import get_customer
from app.tools.payment_tools import get_payment
from app.tools.logging_tools import get_logs


def investigation_agent(state):

    order_id = state["order_id"]

    order = get_order(order_id)

    customer = get_customer(
        order["customer_id"]
    )

    payment = get_payment(order_id)

    logs = get_logs(order_id)

    return {

        "order_data": order,

        "customer_data": customer,

        "payment_data": payment,

        "logs": logs["logs"],

        "customer_id": order["customer_id"],
    }