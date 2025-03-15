these files will start a new angular project 
please note that after coping you file to a Linux vm you need to run this command:
sed -i -e 's/\r$//' entrypoint.sh
after you can run docker-compose and you will get the template when you access http://localhost:4200/
(it may take a few minutes to start running)