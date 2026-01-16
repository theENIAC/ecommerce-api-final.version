from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

# Order  işlemleri için router tanımı
# prefix ile tüm sipariş endpointleri /orders ile başlar
# tags ile de Swagger arayüzünde gruplama sağlar

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)
# Tüm siparişleri listeleyen endpoint
@router.get("/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)
# ID'ye göre tek bir siparişi getiren endpoint
@router.get("/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı")
    return order
# Yeni bir sipariş oluşturan endpoint
@router.post("/", response_model=schemas.Order, status_code=status.HTTP_201_CREATED)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)
# ID'ye göre sipariş silen endpoint
# 204 No Content: işlem başarılı fakat geri dönüş verisi yok dmektir
@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    success = crud.delete_order(db=db, order_id=order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı")
    return None
# Sipariş durumunu güncelleyen endpoint
@router.patch("/{order_id}", response_model=schemas.Order)
def update_order_status(order_id: int, status_update: schemas.OrderStatusUpdate, db: Session = Depends(get_db)):
    updated = crud.update_order_status(db=db, order_id=order_id, status_update=status_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Sipariş bulunamadı")
    return updated
 # Güncellenecek sipariş bulunamazsa hata döndürülürme exception handling ksımı

