# Containerized-EdgeComputing
Although cloud computing as a centralized system has been established successfully, it still faces problems such as high latency and congestion in the network. Edge computing moves to a decentralized system which would reduce the prob- lems faced by cloud computing. Our implementation focuses on the use of containers as a method for edge computing

Docker installation on EC2 instance: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

Containerization of a python/redis application: https://code.tutsplus.com/tutorials/easily-deploy-redis-backed-web-apps-with-docker--cms-20405

Smart home application simulation credits: https://github.com/So-Cool/SHgen

Put each folder in a seperate container and name it as selvasel/<folder-name>

Application deployment commands
```
sudo docker run -t -i -p 8000:8080 selvasel/pyredis /bin/bash /pyredis/launch.sh
sudo docker run -t -i -p 8001:8010 selvasel/numberserver /bin/bash /numberserver/launch.sh
sudo docker run -t -i -p 8002:8020 selvasel/secondserver /bin/bash /secondserver/launch.sh
python client/app.py
```
