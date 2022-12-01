import requests
import typer

from typing import List, Optional

app = typer.Typer(help="Client to manage a ansible wormhole")
version = "0.0.1"


@app.command("mirror")
def mirror(
        roles: Optional[List[str]] = typer.Option(
            [], "--role", "-r", help="OPTIONAL,MULTI-USE - e.g. geerlingguy.ansible"
        ),
        collections: Optional[List[str]] = typer.Option(
            [], "--collection", "-c", help="OPTIONAL,MULTI-USE - e.g. osism.validations"
        )
):
    """
    Mirror ansible roles and collections from upstream ansible galaxy

    Example call: python3 main.py mirror osism.sonic osism.validations
    """
    url = 'http://localhost/api/mirror'
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


def main():
    app()


if __name__ == "__main__":
    main()
