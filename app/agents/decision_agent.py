def decision_agent(state):

    payment = state["payment_data"]

    if payment["status"] == "DECLINED":

        diagnosis = (
            "The order failed because the payment "
            "authorization was declined."
        )

        recommendation = (
            "Ask the customer to update their payment "
            "method and retry the order."
        )

        requires_human = False

    else:

        diagnosis = (
            "No payment failure was detected."
        )

        recommendation = (
            "Further investigation may be required."
        )

        requires_human = True

    return {

        "diagnosis": diagnosis,

        "recommendation": recommendation,

        "requires_human": requires_human,
    }