def response_agent(state):

    order_id = state["order_id"]

    diagnosis = state["diagnosis"]

    recommendation = state["recommendation"]

    return {

        "final_response": (
            f"Order #{order_id} investigation complete.\n\n"
            f"Diagnosis: {diagnosis}\n\n"
            f"Recommended action: {recommendation}"
        )
    }