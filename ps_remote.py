import docker
client = docker.from_env()

containers = client.containers()

print containers