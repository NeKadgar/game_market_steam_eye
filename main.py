import graphene
from fastapi import FastAPI
from celery.result import AsyncResult
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from api import dota, parser
from api.dota.graphql import Query
from background.tasks.parser import pull_history


app = FastAPI(title="Steam Parser")
app.include_router(dota.items.router)
app.include_router(parser.history.router)
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query), on_get=make_graphiql_handler()))


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
