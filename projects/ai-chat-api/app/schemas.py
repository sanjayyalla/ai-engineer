# This file contains all the Pydantic models used by the app.
# Pydantic helps us validate request payloads and shape responses.

from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class ChatMessage(BaseModel):
    # A very simple message model used for chat examples.
    role: Literal["user", "assistant", "system"] = "user"
    content: str = Field(..., min_length=1, max_length=2000)


class ChatRequest(BaseModel):
    # This is the request payload for the /chat endpoint.
    # Pydantic validates the data before the endpoint runs.
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)

    message: str = Field(..., min_length=1, max_length=500)
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    max_tokens: int = Field(default=50, gt=0, le=5000)
    role: Literal["user", "assistant", "system"] = "user"
    metadata: dict[str, str] = Field(default_factory=dict)

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        # Custom validator example.
        # We can add custom business rules to our normal field validation.
        if "hack" in value.lower():
            raise ValueError("Message content looks invalid.")
        return value


class ChatResponse(BaseModel):
    # Response model used to send a predictable JSON response.
    answer: str
    model_used: str = "claude-opus-5.5"
    confidence: float = Field(..., ge=0.0, le=1.0)


class SearchQuery(BaseModel):
    keyword: str = Field(..., min_length=1, max_length=100)
    limit: int = Field(default=5, gt=0, le=20)


class UserProfile(BaseModel):
    # Model with stronger validation rules.
    id: int = Field(gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    role: Literal["admin", "user", "guest"]


class ItemCreate(BaseModel):
    # Example model for creating a resource.
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    in_stock: bool = True


class ItemResponse(BaseModel):
    # Response schema for an item record.
    id: int
    name: str
    price: float
    in_stock: bool


class LoginRequest(BaseModel):
    # Example login payload.
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=6, max_length=50)


class LoginResponse(BaseModel):
    # Example login response.
    access_token: str
    token_type: str = "bearer"
