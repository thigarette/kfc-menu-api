from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from data import crud, models, schemas
from data.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/categories", response_model=List[schemas.Category])
def get_categories(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = crud.get_category_by_name(db, category_name=category.name)
    if new_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db=db, category=category)

@app.get("/menu-items", response_model=List[schemas.MenuItem])
def get_menu_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 50):
    menu_items = crud.get_menu_items(db, skip=skip, limit=limit)
    return menu_items

@app.post("/menu-items/{category_id}", response_model=schemas.MenuItem)
def create_menu_item(menu_item: schemas.MenuItemCreate, category_id: int, db: Session = Depends(get_db)):
    return crud.create_menu_item(db, menu_item, category_id)