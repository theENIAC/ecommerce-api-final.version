[![CI](https://github.com/theENIAC/ecommerce-api-final.version/actions/workflows/ci.yml/badge.svg)](https://github.com/theENIAC/ecommerce-api-final.version/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/theENIAC/ecommerce-api-final.version/branch/main/graph/badge.svg)](https://codecov.io/gh/theENIAC/ecommerce-api-final.version)

## Proje Açıklaması
Hocam merhaba, geliştirmiş olduğum bu proje; FastAPI ile yazılmış, 5 farklı kaynak içeren bir REST API'dir:
- users
- products
- orders
- categories
- reviews

## İlişkiler:
- User → Order (one-to-many)
- Order → Product (many-to-many)
- Product → Category (many-to-one)
- Product → Review (one-to-many)
Tüm kaynaklarda tam CRUD (Create, Read, Update, Delete) işlemleri desteklenmektedir.
Uygun HTTP durum kodları (200, 201, 404, 422 vb.) kullanılmıştır.

## Kullanılan Teknolojiler:
Backend: Python 3 + FastAPI
Veritabanı: SQLite + SQLAlchemy (ORM)
Test: Pytest + pytest-cov
Dokümantasyon: FastAPI built-in Swagger UI (OpenAPI 3.0)
CI/CD: GitHub Actions + Codecov (otomatik test ve coverage raporu)

## Kurulum Talimatları
1. **Repoyu klonlama** (GitHub'dan indirin):
https://github.com/theENIAC/ecommerce-api-final.version
cd ecommerce-api-final.version
2. **Sanal ortam oluşturma ve aktif etme**
python -m venv venv

Windows için:
.\venv\Scripts\activate
Mac/Linux için:
source venv/bin/activate

3. **Gerekli kütüphaneleri yükleme** :
pip install -r requirements.txt
4. **Uygulamayı çalıştırma** (FastAPI sunucusu başlar):
uvicorn main:app --reload

Uygulama varsayılan olarak şu adreste çalışır:
http://127.0.0.1:8000

5. **Testleri çalıştırma**:
pytest -q

6. **Coverage Raporu İçin**
pytest --cov=app -q


## API Dokümantasyonu
Uygulama çalıştığında interaktif Swagger UI arayüzüne şu adresten ulaşabilmektedir:

Swagger UI: http://127.0.0.1:8000/docs


## API Endpoint Listesi ve Örnekler

## Users (Kullanıcılar)
GET /users/
Açıklama: Tüm kullanıcıları listeler (sayfalama destekli).
Örnek: /users/?skip=0&limit=10 → ilk 10 kullanıcıyı getirir.

GET /users/{user_id}
Açıklama: Belirtilen ID'li kullanıcıyı getirir.
Örnek: /users/5 → ID'si 5 olan kullanıcı detayını döner.

POST /users/
Açıklama: Yeni kullanıcı oluşturur.
Örnek:
{
  "username": "ahmet123",
  "email": "ahmet@example.com"
}

PATCH /users/{user_id}
Açıklama: Kullanıcı bilgilerini kısmi olarak günceller.
Örnek:
{
  "username": "yeni_ahmet"
}

DELETE /users/{user_id}
Açıklama: Belirtilen kullanıcıyı siler (204 döner).

## Categories (Kategoriler)

GET /categories/
Açıklama: Tüm kategorileri listeler.
POST /categories/
Açıklama: Yeni kategori oluşturur.
Örnek:
{
  "name": "Elektronik"
}

GET /categories/{category_id}
Açıklama: Tek kategori detayını getirir.
PATCH /categories/{category_id}
Açıklama: Kategori adını günceller.
Örnek:
{
  "name": "Yeni Elektronik"
}

DELETE /categories/{category_id}
Açıklama: Kategoriyi siler.

## Products (Ürünler)

GET /products/
Açıklama: Tüm ürünleri listeler.
POST /products/
Açıklama: Yeni ürün ekler.
Örnek:
{
  "name": "Akıllı Telefon",
  "price": 12000,
  "category_id": 1
}

GET /products/{product_id}
Açıklama: Tek ürün detayını getirir.
PATCH /products/{product_id}
Açıklama: Ürün bilgilerini kısmi günceller.
Örnek:
{
  "price": 11000,
  "name": "Yeni Akıllı Telefon"
}

DELETE /products/{product_id}
Açıklama: Ürünü siler.

## Reviews (Yorumlar)

GET /reviews/
Açıklama: Tüm yorumları listeler.
POST /reviews/
Açıklama: Yeni yorum ekler.
Örnek:
{
  "text": "Çok sağlam ürünmüş cidden, tavsiye ederim!",
  "product_id": 3
}

GET /reviews/{review_id}
Açıklama: Tek yorum detayını getirir.
PATCH /reviews/{review_id}
Açıklama: Yorum metnini günceller.
Örnek:
{
  "text": "Çok güzelbi ürün, ayrıca satıcıdan da memnun kaldım"
}

DELETE /reviews/{review_id}
Açıklama: Yorumu siler.

## Orders (Siparişler)

GET /orders/
Açıklama: Tüm siparişleri listeler.
POST /orders/
Açıklama: Yeni sipariş oluşturur.
Örnek:
{
  "user_id": 1,
  "product_ids": [2, 5]
}

GET /orders/{order_id}
Açıklama: Tek sipariş detayını getirir (ürünler dahil).
DELETE /orders/{order_id}
Açıklama: Siparişi siler (iptal eder).
PATCH /orders/{order_id}
Açıklama: Sipariş durumunu günceller.
Örnek:
{
  "status": "processing"
}


## Test Çalıştırma
- pytest -q

## Coverage Raporu İçin
pytest --cov=app -q


## CI/CD
Her push/pull request'te testler otomatik çalışır (GitHub Actions)
Coverage raporu Codecov ile takip edilebilmektedir.
