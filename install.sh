#!/bin/bash
sudo apt-get update
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management

sudo apt install python3-pip

pip3 install grpcio
pip3 install grpcio-tools
pip3 install protobuf==3.20.*
pip3 install flask
pip3 install pika