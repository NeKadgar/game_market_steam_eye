from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_session
from background.tasks.parser import pull_steam_history
from steam.steam_client import SteamClient
from repository.dota import get_all_item_names

client = SteamClient(cookies={'steamLoginSecure': '76561198380578038%7C%7CB03490B37E984F8F9BCF0FA131D8841E4C25FA07'})

router = APIRouter(
    prefix="/parser",
    tags=["parser"]
)


@router.get("/history",)
def parse_all_items_history(db: Session = Depends(get_session)):
    """Will create parse old steam history tasks!

    DON'T USE IT TWICE!!!!
    """
    for item_hash_name, item_id in get_all_item_names(db):
        pull_steam_history.delay(item_hash_name=item_hash_name, item_id=item_id)
