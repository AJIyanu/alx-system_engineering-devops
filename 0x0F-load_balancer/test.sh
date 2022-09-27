#!/usr/bin/env bash

echo -e  "frontend myfrontend' txt.txt
\tbind 127.0.0.1:80' txt.txt
\tdefault_backend myservers

backend myservers
\tserver server1 127.0.0.1:8000" | tee -a txt.txt
