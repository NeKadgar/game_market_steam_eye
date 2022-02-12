from db.database import SessionLocal, engine
from db.models import dota_item


dota_item.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.commit()
        db.close()
