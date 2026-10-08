# This router is just for practicing CRUD-style endpoints.
# We keep it separate so the app architecture remains understandable.

from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.dependencies import authenticate
from app.schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

items_db: list[ItemResponse] = [
    ItemResponse(id=1, name="Laptop", price=999.99, in_stock=True),
    ItemResponse(id=2, name="Mouse", price=25.5, in_stock=False),
]


@router.get("/", response_model=list[ItemResponse])
async def list_items(
    _authenticated: Annotated[bool, Depends(authenticate)],
    limit: Annotated[int, Query(ge=1, le=20)] = 10,
) -> list[ItemResponse]:
    # FastAPI automatically validates numeric query parameters.
    return items_db[:limit]


@router.post(
    "/",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(
    payload: ItemCreate,
    _authenticated: Annotated[bool, Depends(authenticate)],
) -> ItemResponse:
    # This simulates new data insertion.
    new_item = ItemResponse(
        id=len(items_db) + 1,
        name=payload.name,
        price=payload.price,
        in_stock=payload.in_stock,
    )
    items_db.append(new_item)
    return new_item
