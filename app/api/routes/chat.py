from fastapi import APIRouter


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("")
def chat(message: dict):

    return {
        "message": message,
        "response": "Chat endpoint is working."
    }