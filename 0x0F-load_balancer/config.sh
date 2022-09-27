#!/usr/bin/env bash
# automate inside server

sudo apt update -y
sudo apt upgrade -y
sudo apt-get install -y puppet
puppet apply 7-puppet_install_nginx_web_server.pp
