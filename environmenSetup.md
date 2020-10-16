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

## Install homebrew 

follow https://brew.sh

## Install software with homebrew

    brew install nginx mysql@5.6 redis memcached rabbitmq node graphicsmagick python@3.8
    brew install ffmpeg --with-libvpx --with-libvorbis --with-libx265
    brew cask install google-chrome intellij-idea-ce mysqlworkbench slack

## Download repos

from https://github.com/6connexsource
clone the repos {webapp, event, realtimeserver}






