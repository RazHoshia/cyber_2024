the file will create a docker that runs mysql db with the db mydatabase on it
we have 2 users: myuser, root we can login with password - P@ssw0rd 
because it is only for tests i dont mind sharing the password.

to connect to db i run this command 
to have a table we will run this command:
mysql -h <ip-address-of-vm> -P 3306 -u myuser -p mydatabase

i wanted to have a table to look to so i run these commands:

sudo docker exec -it mysql_db mysql -u myuser -p mydatabase

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    age INT
);

INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 25);

to query the data i did:
SELECT * FROM users;
