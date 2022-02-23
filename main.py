from fastapi import FastAPI
from celery.result import AsyncResult

from api import dota, parser
from background.tasks.parser import pull_history


app = FastAPI(title="Steam Parser")
app.include_router(dota.items.router)
app.include_router(parser.history.router)


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
