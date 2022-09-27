#!/usr/bin/env bash

sed -a 'frontend myfrontend' txt.txt
sed -a '\\\tbind 127.0.0.1:80' txt.txt
sed -a '\\\tdefault_backend myservers\n' txt.txt

sed -a 'backend myservers' txt.txt
sed -a '\\\tserver server1 127.0.0.1:8000' txt.txt
