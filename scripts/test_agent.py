from app.graph.workflow import build_workflow


workflow = build_workflow()


result = workflow.invoke(
    {
        "user_query": "Why did order 10452 fail?",
        "order_id": "10452",
    }
)


print("\nFINAL RESPONSE")
print("=" * 60)
print(result["final_response"])