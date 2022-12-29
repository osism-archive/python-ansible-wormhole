# Wormhole client

Used to add collections and roles to the mirror.

## Usage

Basically use this:

```sh
python3 main.py --help
```

Mirror two collections and one role:

```sh
python3 main.py --wormhole-endpoint http://1.2.3.4 mirror -c osism.services -c osism.validations -r geerlingguy.ansible
```

You might also set the wormhole endpoint via an environment variable:

```sh
export WORMHOLE_ENDPOINT="http://1.2.3.4"
```
