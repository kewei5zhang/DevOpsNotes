# Description

This is to demo how to use docker-compose to manage multiple services.

# TLDR;
```
./run.sh
```
# Install docker compose
```
./install-docker-compose.sh
```

# Build
Build all the Dockerfiles.
```
docker-compose build
```
Note that if your docker compose is version 2, you need to type
```
docker compose build
```
See https://docs.docker.com/compose/reference/

# Run
Run all the containers with dependencies.
```
docker-compose up
```
Note that if your docker compose is version 2, you need to type
```
docker compose up
```

- You can use http://localhost?city=au to use citymatcher
- You can use http://localhost:8080 to use nginx static website

![Alt text](sample.png?raw=true)

# Cleanup
Ctrl+C to stop 

or 
```
docker-compose down
```
Note that if your docker compose is version 2, you need to type
```
docker compose down
```