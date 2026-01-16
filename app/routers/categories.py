from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

# Category işlemleri için router tanımı yapılır
# prefix ile tüm endpointlerin /categories ile başlamasını sağlar
# tags ile  Swagger arayüzünde kategorilendirme için kullanılır 

router = APIRouter(
    prefix="/categories",
    tags=["categories"]# Tüm kategorileri listeleyen endpoint
)

# skip ve limit parametreleri sayfalama amacıyla kullanılır

@router.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

# ID’ye göre tek bir kategori getiren endpoint

@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id=category_id)
        # Eğer kategori bulunamazsa 404 hatası döndürülür
    if category is None:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return category
# Yeni kategori oluşturan endpoint
@router.post("/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)
# Var olan bir kategoriyi güncelleyen endpoint
@router.patch("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category_update: schemas.CategoryCreate, db: Session = Depends(get_db)):
    updated = crud.update_category(db=db, category_id=category_id, category=category_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return updated
# ID’ye göre kategori silen endpoint
@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(db=db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return None
