# NetworkQuiz
Two player quiz game which can be played over a network. Game starts after both players are ready. Both players a given a set of questions which are to answered in a specified time. At the end,the player with maximum score wins.
The game is based on client server model and uses TCP sockets. 

**Prerequisites**
* pandas 
* json

**Running**
* Change the IP addresses of the client and server script to match the IP address of the server.
* Run the server 
```python3 server.py```
* Connect two clients (Players)
```python3 client.py```
* Additional Questions can be added to questions.csv.
