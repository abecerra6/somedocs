# Dev Environment Setup Guide

## Download from Google Drive 

https://drive.google.com/drive/folders/1wAQtaFHkOruJR1dGGFcTb6PAdkKWdLTr

* tomcat-8.5.6
* apache-maven-3.2.1
* JDK-8u261 
* m2.zip
* .bash_profile
* opt folder contents
* nginx folder contents
* from latest_6connexdb: DW_felipe.sql, db_felipe.sql

## Manually install packages

* install downloaded JDK 
* extract tomcat-8.5.6 and apache-maven into /opt
* put /opt/{rts,nfs} from google drive into /opt
* extract m2.zip, move it to /Users/yourUser
* Put the following option into .m2/settings.xml

```
    <server>
      <id>builder2</id>
      <username>dev</username>
      <password>dev2014@china</password>
    </server>
    <server>
      <id>central</id>
      <username>dev</username>
      <password>dev2014@china</password>
    </server>
```
    • Update the `cdn` table in 6connex_db
            
id
vendor
             url
support_ssl
1
Local CDN
https://demo.6connexlocal.com/upload/
1
2
Local CDN (Secure)
https://demo.6connexlocal.com/upload/
1

## Install homebrew 

follow https://brew.sh

## Install software with homebrew

    brew install nginx mysql@5.6 redis memcached rabbitmq node graphicsmagick python@3.8
    brew install ffmpeg --with-libvpx --with-libvorbis --with-libx265
    brew cask install google-chrome intellij-idea-ce mysqlworkbench slack

## Download repos

from https://github.com/6connexsource
clone the repos {webapp, event, realtimeserver}

## Compile the platform

    export PATH for mvn

Run the install.bat in following folders in order:

1. webapp/messaging/install.bat
2. event/install.bat
3. webapp/install.bat
    
## Configure files

Add to your /etc/hosts 

```
127.0.0.1 demo.6connexlocal.com
127.0.0.1 tracking.6connexlocal.com
127.0.0.1 rtsl.6connexlocal.com
```

Move file “Config Files/nginx/nginx.conf” to your local nginx folder /usr/local/etc/nginx/ngnix.conf

Open ngix.conf make sure you have the following lines:

```
access_log  /usr/local/var/log/nginx/access.log  main;
error_log  /usr/local/var/log/nginx/error.log  debug;
```

Copy the following files from google drive folder “Config Files/nginx/ssl-local.*” to your local nginx folder
    
Do:
```
    chmod -R 777 /opt/rts
    chmod -R 777 /opt/nfs
    touch /opt/tomcat/tracking.deploy
```  
  
Go to file /opt/tomcat/conf/server.xml. Replace the path:
```
    /Users/sunny/Workspace/6Connex/
```
with your local code path (e.g)
```
    /Users/yourUser/devel/ 
```

Go to file /opt/tomcat/conf/context.xml. Replace the username and password to your mysql user and password
```
 user="root"
 password="1234"
```

## Setup Database

* Configure a user with password to access the database
* Create databases

```
CREATE DATABASE 6connex_dw2; 
CREATE DATABASE 6connex_db;
```

* Create databases structure

```
mysql -u root -p123456 6connex_dw2 < DW_felipe.sql
mysql -u root -p123456 6connex_db < db_felipe.sql
```
     
You may have to run a list of sql files stored in /webapp/misc/scripts/db/alter_scripts/dw and /webapp/misc/scripts/db/alter_scripts/db

* Update the `cdn table` in 6connex_db
            
| id | vendor | url | support_ssl |
|----|--------|-----|-------------|
| 1  | Local CDN | https://demo.6connexlocal.com/upload/ | 1 |
| 2  |Local CDN (Secure) | https://demo.6connexlocal.com/upload/ | 1 |


* Update the `real_time_server` table in 6connex_db

| id | name | url | active |
|----|--------|-----|-------------|
| 1  | Real Time Server | localhost:8000 | 1 |

