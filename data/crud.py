from sqlalchemy.orm import Session

from . import models, schemas

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_name(db: Session, category_name):
    return db.query(models.Category).filter(models.Category.name == category_name).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_menu_items(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.MenuItem).offset(skip).limit(limit).all()

def get_menu_items_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 50):
    return db.query(models.MenuItem).filter(models.MenuItem.category_id == category_id).offset(skip).limit(limit).all()

def get_menu_item(db: Session, menu_item_id):
    return db.query(models.MenuItem).filter(models.MenuItem.id == menu_item_id).first()

def create_menu_item(db: Session, menu_item: schemas.MenuItemCreate, category_id):
    new_menu_item = models.MenuItem(**menu_item.dict(), category_id=category_id)
    db.add(new_menu_item)
    db.commit()
    db.refresh(new_menu_item)
    return new_menu_item

