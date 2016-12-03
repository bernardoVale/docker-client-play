from docker import Client

# Make sure to enable tcp binding for docker
# Docs: https://docs.docker.com/engine/reference/commandline/dockerd/
# Version auto to force Server:Client API match
cli = Client(base_url='tcp://54.158.84.84:2375', version='auto')

all_containers = cli.containers(all=True)

for container in all_containers:
    print container