#!/bin/bash
python3 ./rpc/worker.py & 

python3 ./mom/worker1/worker1.py & 

python3 ./mom/worker2/worker2.py &

python3 ./gateWay/apiGateWay.py  
