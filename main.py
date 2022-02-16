from scrape import getCategories, getItems

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

streetwise_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=hawugh3xujtc0407&ItemSearch%5Bday%5D=7'
snacks_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=0anomwm9jcnozryg&ItemSearch%5Bday%5D=7'
sharing_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=njl5ulycgg8ft5rv&ItemSearch%5Bday%5D=7'
chicken_deals_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=c5x4llcdlwtk0nok&ItemSearch%5Bday%5D=7'
side_items_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=hrg3adkvuhe68spw&ItemSearch%5Bday%5D=7'
drinks_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=0ffdg0xcq9ebcicn&ItemSearch%5Bday%5D=7'
amazing_deals_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=csuaancja9hevwig&ItemSearch%5Bday%5D=5'
urls_list = [
    streetwise_url,
    snacks_url,
    sharing_url,
    chicken_deals_url,
    side_items_url,
    drinks_url,
] 

@app.get("/scrape")
def scrape_kfc_website(db: Session = Depends(get_db)):    
    for url in urls_list:
        new_category = crud.get_category_by_name(db, category_name=getCategories(url))
        if new_category == None:
            # raise HTTPException(status_code=400, detail="Category already exists")
            category: schemas.CategoryCreate = schemas.CategoryCreate(name=getCategories(url))
            crud.create_category(db=db, category=category)

    message = "Scrape was successful and data was inserted into the db"
    response = {
        "message": message
    }
    return response

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