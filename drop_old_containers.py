from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

containers = cli.containers(filters={'status': 'exited'})

# Iterate all containers that has status Exited and execute `docker rm` on them
for container in containers:
    cli.remove_container(container=container['Id'])