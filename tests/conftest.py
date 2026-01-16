import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from app.database import Base, get_db
from app.models import Base as ModelsBase  # Model'lerin Base'i

# Test için ayrı veritabanı (ana veri tabanını bozmasın)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_test.db"  # Farklı isim verdim ki karışmasın

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# temiz ortam oluşturmak için
@pytest.fixture(scope="function")
def db_session():
    # Testten önce tablolar oluşturulur
    ModelsBase.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    yield db

    # Test bittikten sonra veritabanı temizlenir
    db.close()

    ModelsBase.metadata.drop_all(bind=engine)  # Temizleme kısmı

# Test için API client'ı
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
