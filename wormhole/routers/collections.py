import glob
import os
from fastapi import APIRouter
from ..settings import settings

router = APIRouter()
base_url = settings.base_url


@router.get('/api/v2/collections/{owner}/{collection}/')
async def get_collection(owner: str, collection: str) -> dict:
    return {}


@router.get('/api/v2/collections/{owner}/{collection}/versions/')
async def get_collection_versions(owner: str, collection: str) -> dict:
    path = f"/mirror/collections/{owner}-{collection}-*.tar.gz"
    file_list = [os.path.basename(file) for file in glob.glob(path)]
    result = []
    for filename in file_list:
        version = filename.split('-')[-1].removesuffix('.tar.gz')
        record = {
            "version": version,
            "href": f"{base_url}/api/v2/collections/{owner}/{collection}/versions/{version}/"
        }
        result.append(record)
    return {
        "results": result
    }


@router.get('/api/v2/collections/{owner}/{collection}/versions/{version_number}/')
async def get_collection_version(owner: str, collection: str, version_number: str) -> dict:
    return {
        "href": f"{base_url}/api/v2/collections/{owner}/{collection}/versions/{version_number}/",
        "download_url": f"{base_url}/download/collections/{owner}-{collection}-{version_number}.tar.gz",
        "artifact": {
            "sha256": ""
        },
        "namespace": {
            "name": f"{owner}"
        },
        "collection": {
            "name": f"{collection}"
        },
        "version": f"{version_number}",
        "metadata": {
            "dependencies": {},
        }
    }
