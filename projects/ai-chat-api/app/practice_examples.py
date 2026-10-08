# This file is a learning notebook in Python form.
# It demonstrates common FastAPI + Pydantic patterns in a simple way.

from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Practice Playground")


class Item(BaseModel):
    """A simple Pydantic model."""

    name: str
    price: float = Field(gt=0)
    in_stock: bool = True


@app.get("/")
def home() -> dict[str, str]:
    # Basic root endpoint: returns a simple JSON response.
    return {"message": "Hello from FastAPI app"}


@app.get("/items")
def list_items(
    limit: Annotated[int, Query(gt=0, le=100)] = 10,
) -> dict[str, list[str] | int]:
    # Query parameters are validated automatically by FastAPI/Pydantic.
    return {"items": ["pen", "book", "laptop"], "limit": limit}


@app.post("/items")
def create_item(item: Item) -> Item:
    # The request body is parsed into the Item model automatically.
    # If the data is invalid, FastAPI returns a 422 validation error.
    return item


@app.get("/greet")
def greet(name: str = "developer") -> dict[str, str]:
    # Path/query parameter examples.
    return {"message": f"Hello, {name}!"}
