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

Use a yaml file (e.g. _mirror.yml_):

```yaml
roles:
  - geerlingguy.ansible
collections:
  - osism.services
  - osism.validations
```

```sh
python3 main.py --wormhole-endpoint http://1.2.3.4 mirror -f mirror.yml
```

A combination of "-c", "-r" and "-f" is also possible.

You might also set the wormhole endpoint via an environment variable:

```sh
export WORMHOLE_ENDPOINT="http://1.2.3.4"
```
