# Ansible Wormhole

Ansible Wormhole is a tool that allows you to mirror roles and collections from the Ansible-Galaxy just like [pulp](https://docs.pulpproject.org/pulpcore/).
But unlike pulp, it is just a mirror for ansible stuff, no additional assets!

This project is still in an early stage, but functional. Comments are welcome!

## Client config for Ansible mirror (collections and roles)

Use the following to pull roles and collections from your wormhole-host:

```sh
ansible-galaxy install elasticsearch,6.2.4 -s https://localhost/
ansible-galaxy collection install 'osism.validations:==0.2.0' -s https://localhost/
```

If your wormhole installation is not secured with SSL you have to allow this within the command:

```sh
ansible-galaxy install elasticsearch,6.2.4 -c -s http://localhost/
ansible-galaxy collection install 'osism.validations:==0.2.0' -c -s http://localhost/
```

Alternatively you can configure this in the various locations of your `ansible.cfg` file (`~/.ansible.cfg`, `/etc/ansible/ansible.cfg`, `./ansible.cfg`):

```ini
[galaxy]
server_list = wormhole, official
#server=https://galaxy.ansible.com/

[galaxy_server.wormhole]
url=http://localhost
validate_certs=false

[galaxy_server.official]
url=https://galaxy.ansible.com/
```

## behind a proxy

If you are using a proxy with a subpath, have a look at the dev.yml file.
An matching example nginx config might look like this:

```sh
    [...]
    upstream wormhole {
        server wormhole:80;
    }

    server {
        [...]
        ## wormhole
        location /wormhole/ {
            proxy_pass http://wormhole/;
        }
        location /ansible {
            default_type        application/json;
        }
```

Keep an eye on the trailing backslash in the location and proxy_pass line. Without them it will probably not work.
