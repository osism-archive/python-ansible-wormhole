import os
import requests
import typer
import yaml

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
    url = f"{settings['api_url']}/ansible/api/mirror"
    if config_file != "":
        with open(config_file, "r") as file:
            data = yaml.safe_load(file)
        roles = roles + data["roles"]
        collections = collections + data["collections"]
    payload = {
        "roles": roles,
        "collections": collections
    }
    result = requests.post(
        url=url,
        json=payload,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    print(result.text)


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
