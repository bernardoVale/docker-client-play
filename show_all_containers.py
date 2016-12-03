from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

all_containers = cli.containers(all=True)

for container in all_containers:
    print container