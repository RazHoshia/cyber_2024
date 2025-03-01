this docker compose will run a server to analyze the data and decide if its allowed or if the data is bad and should in the future be blocked.
until the sql proxy will work properly i tested:
curl -X POST "http://<ip_of_vm_running_the_docker>:5000/analyze" -H "Content-Type: application/json" -d '{"query": "SELECT * FROM users WHERE name = '\''admin'\'' OR '\''1'\''='\''1'\'';"}'
and i got {"action":"block"}
and when I run:
curl -X POST "http://<ip_of_vm_running_the_docker>:5000/analyze" -H "Content-Type: application/json" -d '{"query": "SELECT * FROM users;"}'
I got {"action":"allow"}
both are as excepted, we of course will change the logic later on