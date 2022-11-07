Apache Internal Error (500) Fix

SUMMARY
I was building a site with apache and at Nov 1, 2022 6:00 AM an Internal Server Error Occured
curl -sI 127.0.0.1 will return;
HTTP/1.0 500 Internal Server Error
Date: Tue, 1 Nov 2022 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

This error would not allow the site to be deployed.
After debugging, it was discovered that one of the configuration file has a typo error
class-wp-locale.php was spelt class-wp-locale.php in wp-settings.php
strace revealed that netstat couldnt access the file because it doesnt exist

TIMELINE
Detected at Nov 1, 2022 6:00 AM
Detected while trying to have a preview of site before deployment
It was resolved making an strace on the apache server and trying to curl the ip

ROOT CAUSE AND RESOLUTION
procedure to detecting and fixing errror are listed below
1. tried to check apache status on ubuntu, it returned active
2. restarted the service and it restarted without errors
3. opened two terminals did an strace on www-data pid on one terminal and curl the IP on another terminal
4. this revealed that telstat can't access class-wp-locale.php because it does not exist
5. that is definitely some typo error and it is important to know while file has this typo
6. with grep, I made a search on all configuration file to find which has error and returned wp-settings.php
7. I fixed the typo error and curl returned 200 ok.
8. I wrote a puppet automation to fix future error
