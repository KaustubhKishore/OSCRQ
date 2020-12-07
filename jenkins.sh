# shellcheck disable=SC2046
docker stop $(docker ps -aq) 2> /dev/null || true
docker rm $(docker ps -aq) 2> /dev/null || true
docker run -d -p 3000:3000 lordrevolta/capdash:latest