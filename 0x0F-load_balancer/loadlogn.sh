#!/usr/bin/env bash
# upload configuration file to a server

scp ~/AJIyanu/alx-system_engineering-devops/0x0F-load_balancer/7-puppet_install_nginx_web_server.pp ubuntu@$1:~/
ssh ubuntu@$1 'bash -s' < config.sh
