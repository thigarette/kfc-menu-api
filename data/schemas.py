from typing import List, Optional

from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItem(MenuItemBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    menu_items: List[MenuItem] = []

    class Config:
        orm_mode = True