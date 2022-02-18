from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from celery.result import AsyncResult

from background.tasks.item_base import update_steam_items
from background.tasks.parser import pull_history
from db import get_session
from repository.dota import create_item, get_item
from schemas.dota_item import DotaItemCreate

app = FastAPI()


@app.get("/")
async def status(item_hash_name: str) -> dict:
    task = pull_history.delay(item_hash_name, 1)
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_status(task_id: str) -> dict:
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result


@app.post("/item")
async def test_create_item(item: DotaItemCreate, db: Session = Depends(get_session)):
    item = create_item(db, item)
    return item


@app.post("/item/task")
async def test_create_item(item: DotaItemCreate):
    item = update_steam_items.delay(item.name)
    return item.id


@app.get("/item/{pk}")
async def test_get_item(pk: int, db: Session = Depends(get_session)):
    item = get_item(db, pk)
    return item
