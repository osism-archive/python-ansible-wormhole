import os
import requests
import typer
import yaml

from rich.progress import track
from typing import List, Optional

app = typer.Typer(help="Client to manage a ansible wormhole")
version = "0.0.1"
os.environ
settings = {"api_url": os.getenv("WORMHOLE_ENDPOINT", "http://localhost")}


@app.command("mirror")
def mirror(
        roles: Optional[List[str]] = typer.Option(
            [], "--role", "-r", help="OPTIONAL,MULTI-USE - e.g. geerlingguy.ansible"
        ),
        collections: Optional[List[str]] = typer.Option(
            [], "--collection", "-c", help="OPTIONAL,MULTI-USE - e.g. osism.validations"
        ),
        config_file: Optional[str] = typer.Option(
            "", "--file", "-f", help="OPTIONAL,SINGLE-USE - e.g. mirror.yml"
        )
):
    """
    Mirror ansible roles and collections from upstream ansible galaxy

    Example call: python3 main.py mirror osism.sonic osism.validations
    """
    url = f"{settings['api_url']}/api/mirror"
    if config_file != "":
        with open(config_file, "r") as file:
            data = yaml.safe_load(file)
        roles = roles + data["roles"]
        collections = collections + data["collections"]

    for role in track(roles, description="Processing Roles...", total=None):
        result = requests.post(
            url=url,
            json={
                "roles": [role],
                "collections": []
            },
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        print(f"{role}: {result.text}")
    for collection in track(collections, description="Processing Collections...", total=None):
        result = requests.post(
            url=url,
            json={
                "roles": [],
                "collections": [collection]
            },
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        print(f"{collection}: {result.text}")

    # The API is actually capable of handling all in just one call.
    # But the progress bar is a benefit for the user in my opinion.
    #payload = {
    #    "roles": roles,
    #    "collections": collections
    #}
    #result = requests.post(
    #    url=url,
    #    json=payload,
    #    headers={
    #        "accept": "application/json",
    #        "Content-Type": "application/json"
    #    }
    #)
    #print(result.text)


@app.command("version")
def version():
    print(version)


@app.callback()
def generic(
        url: Optional[str] = typer.Option(
            "http://localhost", "-w", "--wormhole-endpoint"
        )):
    settings['api_url'] = url.strip("/")


def main():
    app()


if __name__ == "__main__":
    main()
