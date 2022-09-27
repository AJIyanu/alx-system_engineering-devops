#!/usr/bin/env bash
# login into servers with ubuntu as username

if [[ $# -eq 1 ]]
then
	ssh ubuntu@$1
else
	echo "usage: login <server ip>"
fi
