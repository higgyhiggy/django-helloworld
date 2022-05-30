sudo docker kill $(sudo docker ps -q)

sudo docker build --tag python-django3 .

sudo docker run --publish 8000:8000 -d python-django3
