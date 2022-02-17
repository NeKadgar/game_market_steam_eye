from db.database import SessionLocal, engine
from db.models import dota_item


def get_session():
    with SessionLocal() as session:
        yield session
