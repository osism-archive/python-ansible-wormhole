import requests

from fastapi import APIRouter

router = APIRouter()


# TODO enable pagination
@router.post('/api/mirror')
async def mirror_roles(payload: dict) -> dict:
    for role_name in payload['roles']:
        owner, role = role_name.split('.')
        url = "https://galaxy.ansible.com/api/v1/roles/"
        query = {"owner__username": owner, "name": role}
        role_id = requests.get(url, params=query).json()['results'][0]['id']
        url = f"https://galaxy.ansible.com/api/v1/roles/{role_id}/versions/"
        results = requests.get(url).json()['results']
        for result in results:
            download_url = result['download_url']
            version_name = result['version']
            version_id = result['id']
            response = requests.get(download_url)
            with open(f"/mirror/roles/{role_id}-{owner}-{role}-{version_name}-{version_id}.tar.gz", "wb") as file:
                file.write(response.content)
            del response

    for collection_name in payload['collections']:
        owner, collection = collection_name.split('.')
        url = f"https://galaxy.ansible.com/api/v2/collections/{owner}/{collection}/versions/"
        results = requests.get(url).json()['results']
        for result in results:
            href = result['href']
            version = result['version']
            download_url = requests.get(href).json()['download_url']
            response = requests.get(download_url)
            with open(f"/mirror/collections/{owner}-{collection}-{version}.tar.gz", 'wb') as file:
                file.write(response.content)
            del response

    return {
        "status": "ok"
    }
