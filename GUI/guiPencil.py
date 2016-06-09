#____ Bibliotecas ____#
from tkinter import *
from threading import Thread
import tkinter.messagebox
import threading
import time
import os
import random
import socket
import tkinter.scrolledtext



class myClient(Thread):
	host="192.168.4.1"
	port=80
	size=1024
	mySock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def __init__(self,new_window):
		super(myClient, self).__init__()
		self.window=new_window
		self.Connexion=False

	def listen(self):
		message=""
		if self.Connexion:
			data=b''
			while(not '\n' in message):
				data=self.mySock.recv(self.size)
				message+=data.decode()

		return message

	def send(self,message):
		if self.Connexion:
			mns=message.encode()
			try:
				self.mySock.send(mns)
			except:
				self.Connexion=False
			

	def connect(self):
		server_address=(self.host,self.port)
		try:
			self.mySock.connect(server_address)
			self.window.show("Connexion Success\n")
			self.Connexion=True
			return True
		except:
			self.window.show("Error can't connect to Pencilduino server\n")
			return False

	def run(self):
		while True:
			try:
				mns=self.listen()
				self.window.show(mns)
			except:
				self.window.show("Connexion Error, stop listen\n")
				break;
class myDrawingPlace(object):
	def __init__(self,root,width,height):
		self.root = root
		self.width = width
		self.height = height
		self.myCanvas = Canvas(self.root,width=self.width*30,height=self.height*30,bg="gray")
		self.myCanvas.place(x=600,y=100)
		self.matrix = [] 
		self.initMatrix(self.matrix,self.width,self.height)
		self.lastPointX = 0
		self.lastPointY = 0
		self.lastColor = 0
		self.squares = []
		self.squareXY(3,7,1)
		#self.squareXY(3,6,0)
		#self.squareXY(3,8,1)
		self.diagonal("left","down")
		#self.printMatrix(self.matrix,self.width,self.height)
		self.eraseSquares()
	#initialize the matrix 
	def initMatrix (self,matrix,width,height):
		i = 0
		while (i < width):
			j = 0 
			temp = []
			while (j < height):
				temp  = temp + ["gray"]
				j = j + 1	
			self.matrix = self.matrix + [temp]
			i = i + 1
	#print the matrix using the amount of rows and colums
	def printMatrix (self,matrix,width,height):
		i = 0
		while (i < width):
			print (matrix[i]) 
			i = i + 1
	#paint a square using rows and  cols
	def squareXY(self,posx,posy,color):
		if (posx <= self.width and posy <= self.height):
			myColor =  ""
			if (color == 0 ):
				myColor = "blue"
			elif (color == 1 ):
				myColor = "red"
			else:
				myColor = "black"
			self.lastPointX = posx*30
			self.lastPointY = posy*30
			self.lastColor = color
			square = self.myCanvas.create_rectangle(posx*30, posy*30,posx*30+ 30,posy*30 + 30, fill=myColor)
			self.squares = self.squares + [square]
			self.matrix[posx][posy] = [myColor]
		else: 
			print ("Error while painting the square.")
	#diagonal  (right or left , up or down)
	def diagonal (self,directionX,directionY):
		xAxisMovement=0
		yAxisMovement=0
		if (directionX == "right"):
			xAxisMovement = 1
		if (directionY == "down"):
			yAxisMovement = 1
		if  (directionX == "left" ):
			xAxisMovement = -1
		if (directionY == "up"):
			yAxisMovement = -1
		print(xAxisMovement)
		print(yAxisMovement)
		nextXPosition = int((self.lastPointX)/30) + xAxisMovement
		nextYPosition = int((self.lastPointY)/30) + yAxisMovement
		
		while ((nextXPosition < self.width and nextYPosition < self.height) 
													and nextXPosition >= 0 and nextYPosition >= 0 ):
			print("The new position is: " + str (nextXPosition) + " : "+ str(nextYPosition) )
			self.squareXY(nextXPosition,nextYPosition,self.lastColor)
			nextXPosition = nextXPosition + xAxisMovement
			nextYPosition = nextYPosition + yAxisMovement
	def eraseSquares(self):
		if (self.squares == []):
			print ("Nothing to erase")
		else:
			for i in self.squares:
				self.myCanvas.delete(i)
			self.root.update()
class myWindow:
	actual_index=3.0
	def __init__(self):

		self.root=Tk()
		self.root.title('Pencilduino Interpreter')
		self.root.minsize(1200,650)
		self.root.resizable(width=NO,height=NO)
		#Canvas 
		self.lienzo=Canvas(width=1200,height=650,bg='white')
		self.lienzo.place(x=0,y=0)
		
		self.chart = tkinter.scrolledtext.ScrolledText(self.lienzo,width=49,height=25,bg='light green',state='disabled')
		self.chart.place(x=175,y=100)

		self.command_line=Entry(self.lienzo,width=44,font = "Helvetica 12",bg='light grey')
		self.command_line.place(x=175,y=505)

		#label=Label(self.lienzo,text="->")
		self.command_line.bind('<Return>', self.enter)

		btn_connect=Button(self.lienzo, text='CONNECT', command=self.comunicate,bg='white',fg='blue')
		btn_connect.place(x=500,y=30)


		titleLabel = Label(self.lienzo, text = "PencilDuino Interpreter",font = "Helvetica 16",bg='white')
		titleLabel.place(x=180,y=30)

		#Canvas to display the  result
		self.myDP = myDrawingPlace(self.root,15,15)


		#Communication
	def comunicate(self):
		self.Duino=myClient(self)
		if(self.Duino.connect()):
			self.Duino.start()
			

	def enter(self,event):
		if(self.Duino.Connexion==False):
			self.show("Please connect first to server before sending commands\n")
		else:
			message=self.command_line.get()
			if(message!="" or message!=None):
				if(not '\n' in message):
					message+='\n'
				self.Duino.send(message)
				self.show(message)
				self.command_line.delete(0, 'end')


	def show(self,message):
		index=self.actual_index
		if(message!="" or message!=None):
			self.chart.configure(state=NORMAL)
			self.chart.insert(index,"-> "+message)
			self.actual_index+=1.0
			self.chart.configure(state=DISABLED)


	def run(self):
		self.root.mainloop()



