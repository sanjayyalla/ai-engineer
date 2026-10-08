# This file stores reusable dependencies.
# Dependency injection is one of the biggest strengths of FastAPI.
# It allows us to reuse validation logic across multiple endpoints.

from typing import Annotated

from fastapi import Header, HTTPException


def authenticate(
    x_api_key: Annotated[str | None, Header(alias="x-api-key")] = None,
) -> bool:
    # Header validation example.
    # If the client sends the wrong key, we return a 401 response.
    if x_api_key != "secret123":
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
        )

    return True


def get_user_name(x_user_name: Annotated[str | None, Header(alias="x-user-name")] = None) -> str:
    # This demonstrates a custom header-based dependency.
    # In real apps, you might use this to know which user is making the request.
    if not x_user_name:
        return "guest"
    return x_user_name
