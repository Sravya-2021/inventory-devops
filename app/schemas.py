from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
