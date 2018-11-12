```
docker run -it --net=host --env="DISPLAY" -v ~/.Xauthority:/root/.Xauthority:rw -v <path to where the repo is>:/mnt  matplotlib:latest
```
