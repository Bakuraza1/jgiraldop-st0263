#!/bin/bash
sudo apt-get update
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management

sudo apt install python3-pip

sudo pip3 install grpcio
sudo pip3 install grpcio-tools
sudo pip3 install protobuf==3.20.*
sudo pip3 install flask
sudo pip3 install pika