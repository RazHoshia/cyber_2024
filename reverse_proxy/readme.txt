this is the reverse proxy,
from now everyone who wants to query db will do it like that mysql -h 192.168.189.148 -P 6033 -u myuser -p mydatabase
when of course the ip will be the reverse_proxy vm ip!

the script.py will run and log the data, in addition it will send the data to server and will get back the data and the result (blocked or allowed) and will log it.
the script updates querys every  seconds, you can change script for less time.
to see the logs - after starting all the dockers (and once there is a query) we will run sudo docker exec -it proxysql tail -f /app/server_responses.txt

please note:
in script.py there is a line:
 HTTP_SERVER_URL = "http://192.168.189.143:5000/analyze"  
please change the ip to the ip of the vm you are running the analyze server on.
in addition, in the file proxysql.cnf there is a line:
 mysql_servers = (
  { address="192.168.189.142", port=3306, hostgroup=10, max_connections=100 }
please change the ip to the ip of the vm you are running the MySQL db server on.

to query the db through the proxy we will do:
mysql -h 192.168.189.148 -P 6033 -u myuser -p mydatabase