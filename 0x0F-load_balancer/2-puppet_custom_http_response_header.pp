# Install Nginx web server with Puppet

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo service nginx start ; sudo sed -i "63i \\\tadd_header X-Served-By \$hostname;" /etc/nginx/nginx.conf ; sudo service nginx restart',
}
