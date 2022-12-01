import glob
import os

from fastapi import APIRouter
from ..settings import settings

router = APIRouter()
base_url = settings.base_url


@router.get('/api/v1/roles/')
async def get_role(owner__username: str, name: str) -> dict:
    path = f"/mirror/roles/*-{owner__username}-{name}-*.tar.gz"
    file_list = [os.path.basename(file) for file in glob.glob(path)]
    result = []
    for filename in file_list:
        version_name = filename.split('-')[-2].removesuffix('.tar.gz')
        version_id = filename.split('-')[-1].removesuffix('.tar.gz')
        role_id = filename.split('-')[0]
        record = {
            "version": version_id,
            "name": version_name
        }
        result.append(record)

    return {
        "results": [
            {
                "id": role_id,
                "summary_fields": {
                    "versions": result
                }
            },
        ]
    }


@router.get('/api/v1/roles/{id}/versions/')
async def get_role_versions(id: int) -> dict:
    path = f"/mirror/roles/{id}-*.tar.gz"
    file_list = [os.path.basename(file) for file in glob.glob(path)]
    result = []
    for filename in file_list:
        version_name = filename.split('-')[-2].removesuffix('.tar.gz')
        version_id = filename.split('-')[-1].removesuffix('.tar.gz')
        owner = filename.split('-')[1]
        role = filename.split('-')[2]
        record = {
            "id": version_id,
            "name": version_name,
            "download_url": f"{base_url}/download/roles/{id}-{owner}-{role}-{version_name}-{version_id}.tar.gz",
            "active": None
        }
        result.append(record)

    return {
        "results": result
    }
