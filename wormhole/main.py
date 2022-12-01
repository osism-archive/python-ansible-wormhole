import os
from .routers import mirror, roles, collections
from .settings import settings
from fastapi import FastAPI

app = FastAPI()
app.include_router(mirror.router)
app.include_router(roles.router)
app.include_router(collections.router)
base_url = settings.base_url


@app.on_event("startup")
async def preparation() -> None:
    paths = [
        "/mirror/roles",
        "/mirror/collections"
    ]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


@app.get('/api')
async def get_api() -> dict:
    return {
        "description": "Ansible Wormhole REST API",
        "current_version": "v2",
        "available_versions": {
            "v1": "v1/",
            "v2": "v2/"
        },
        "server_version": "0.0.1",
        "version_name": "Offline mirror for Ansible Galaxy",
        "team_members": [
            "tibeer"
        ]
    }
