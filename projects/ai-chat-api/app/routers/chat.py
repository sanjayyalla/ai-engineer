# This router contains chat-related endpoints.
# Keeping endpoints grouped by feature makes the app easier to maintain.

from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies import authenticate, get_user_name
from app.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post(
    "/",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    summary="Send a chat message",
    description="This endpoint validates the request body and returns a simulated chat response.",
)
async def send_chat_message(
    payload: ChatRequest,
    _authenticated: Annotated[bool, Depends(authenticate)],
    user_name: Annotated[str, Depends(get_user_name)],
) -> ChatResponse:
    # This is where a real AI model call would happen.
    # For practice, we just return a simple fake assistant answer.
    answer_text = f"Hello {user_name}, I received: {payload.message}"

    return ChatResponse(
        answer=answer_text,
        confidence=0.92,
    )


@router.get("/history", summary="Get sample chat history")
async def chat_history() -> list[dict[str, str]]:
    # Sample endpoint to show how list responses can be returned.
    return [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi! How can I help?"},
    ]
