import socket                
import json
import pickle
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8080             
  
# connect to the server on local computer 
s.connect(('170.20.10.4', port)) 


timeStart = None
timeEnd = None
totalQuestion=5


def startScreen():
	print("**************WELCOME TO QUIZ GAME**************");
def welcomeMessage():
	while True:
		message = s.recv(1024).decode('utf-8')
		if(message):
			startScreen()
			print(message)
			return
welcomeMessage()

#get the score of the players
def getScore():
	while True:
		score = s.recv(1024)
		if(score):
			global totalQuestion
			totalQuestion=totalQuestion-1
			leaderboard = pickle.loads(score)
			print('\n\t\tYour score', leaderboard["player1"],end='\t\t\t')
			print('Opponent score', leaderboard["player2"])
			if totalQuestion==0:
				print("MATCH RESUTLT: ",end=' ')	
				score1=int(leaderboard["player1"])
				score2=int(leaderboard["player2"])
				if score1>score2:
					print("You won")
				elif score1<score2:
					print("Opponent won")
				else:
					print("Match Tie")
			return
	print('\n')
	

#receive questions from the server
def getQuestion():
	while True:
		question = s.recv(2048).decode('utf-8')
		if(question):
			if(question=="Player 2 Connected! Both players ready"):
				startScreen()
				print(question)
				startTime=datetime.datetime.now()
				endTime=startTime-timedelta(hour=0,minute=10)
				
				print("start time: ",currHour,":",currMinute)
				
				continue
			print(question)
			option=input('Your option: ').encode('utf-8')
			s.send(option)
			while True:
				answer = s.recv(1024).decode('utf-8')
				if(answer):
					print(answer)
					break
			getScore()
		result = "Question completed"
		s.send(result.encode('utf-8'))
	return
		
getQuestion()


print("Closed")
# close the connection 
s.close()  
