this docker compose will run a server to analyze the data and decide if its allowed or if the data is bad and should in the future be blocked.
SQLProxy is working-
the proxy sends data to this server. for now the server will return blocked (and the data) when a user does this query - select * from users limit 5; (and really any number in select * from users limit). 
when the query is ok it will return allow and the data it was sent.
