import pandas as pd 
import socket
from _thread import *
import threading
import pandas as pd
import json
import pickle
import time
import datetime

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creation successfull")

HOST = "172.20.10.4"
PORT = 8080
connectionList = []
score={}
serverSocket.bind(('172.20.10.4',PORT))
print("Server binded to ",str(HOST),":",str(PORT))

serverSocket.listen(10)

def clientThread(conn,addr):
	if(len(connectionList)==1):
		connectionList[0].send("Player 1 connected !! Waiting for player 2")
		while(len(connectionList)==1):
			continue

	message="Player 2 Connected! Both players ready"


	score[conn]=0;
	conn.send(message)
	df=pd.read_csv("questions.csv")
		#print(df.head)
		#print(df.columns)
	index=0
	while(index<5):
		tempdf=df['Question']
		message="Question :" +tempdf.loc[index]+"\n"
			#mesage=message.to_json(orient='values')
		tempdf=df['Option A']
		message+="A: "+tempdf.loc[index]+'\n'
		tempdf=df['Option B']
		message+="B: "+tempdf.loc[index]+'\n'
		tempdf=df['Option C']
		message+="C: "+tempdf.loc[index]+'\n'
		tempdf=df['Option D']
		message+="D: "+tempdf.loc[index]+'\n'
		conn.sendall(message)
		tempdf=df['Correct ans']
		correctAnswer=tempdf.iloc[index]
		answer=None
		while not answer:
			answer=conn.recv(2048).decode('utf-8')
		if answer.lower()==correctAnswer.lower():
			conn.sendall("correct Answer")
			score[conn]=score[conn]+1
		else:
			conn.sendall("Incorrect Answer")
		print(score[conn])
		#scoreString="";
		scoreDict={}
		if(conn==connectionList[0]):
			scoreDict = {"player1":score[conn],"player2":score[connectionList[1]]}
			print("******")
			
		else:
			scoreDict = {"player1":score[conn],"player2":score[connectionList[0]]}
		print(scoreDict)
		serializedDict=pickle.dumps(scoreDict)
		conn.sendall(serializedDict)
		temp=conn.recv(2048)
		index+=1
		#conn.sendall()
		#time.sleep(100);
				
def broadcastMessage(message):
	#message=message.encode('utf-8')
	for conn in connectionList:
		conn.send(message)

def acceptConnections():
	while True:
		conn,addr = serverSocket.accept()
		print("connection established with ",str(addr))
		connectionList.append(conn)
		start_new_thread(clientThread,(conn,addr))

		

acceptConnections()
