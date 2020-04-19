import sys
import os
import signal
import sqlite3
from datetime import datetime
from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial
#you need to run CreateDb() function for the first time to create database file (.db)
#ONLY run CreateDb() function in the first time

def CreateDb():
	con = sqlite3.connect('C://Users//Public//Desktop//Account.db')		
	cur = con.cursor()
	
	# cur.execute('CREATE TABLE Pets(Id INT, Name NVARCHAR, Price NVARCHAR)')
	# cur.execute('INSERT INTO Pets VALUES(1, "Cat", "400$")')
	# cur.execute('INSERT INTO Pets VALUES(2, "Dog", "600$")') 
	# cur.execute('INSERT INTO Pets VALUES(3, "Rabbit", "200$")')
	# cur.execute('INSERT INTO Pets VALUES(4, "Bird", "60$")')

	cur.executescript("""DROP TABLE IF EXISTS Account;
					CREATE TABLE Account(Username VARCHAR, Password VARCHAR, Date NVARCHAR);""")
	con.close()

class UI(object):
	def setupUI(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(300, 300)
		Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Login!", None, -1))
		
		font = QtGui.QFont()
		font.setFamily("MS PMincho")
		font.setPointSize(10)
		font.setWeight(75)
		font.setBold(True)
		
		self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_1.setGeometry(QtCore.QRect(50, 60, 200, 41))
		self.lineEdit_1.setFont(font)
		self.lineEdit_1.setPlaceholderText("Username...")
		self.lineEdit_1.setObjectName("lineEdit_1")
				
		self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_2.setGeometry(QtCore.QRect(50, 120, 200, 41))
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setPlaceholderText("Password...")
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
				
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(100, 200, 100, 23))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Sign In", None, -1))
		self.pushButton.clicked.connect(partial(self.signIn))
		
		self.pushButton1 = QtWidgets.QPushButton(Dialog)
		self.pushButton1.setGeometry(QtCore.QRect(100, 230, 100, 23))
		self.pushButton1.setObjectName("pushButton1")
		self.pushButton1.setText(QtWidgets.QApplication.translate("Dialog", "Sign Up", None, -1))
		self.pushButton1.clicked.connect(partial(self.signUp))
		
		Dialog.show()
		
	def signUp(self):
		font = QtGui.QFont()
		font.setFamily("MS PMincho")
		font.setPointSize(10)
		font.setWeight(75)
		font.setBold(True)
		
		self.dialog1 = QtWidgets.QWidget()
		self.dialog1.setWindowTitle(QtWidgets.QApplication.translate("dialog1", "Sign Up!", None, -1))
		self.dialog1.resize(350, 300)
		
		self.lineEdit_3 = QtWidgets.QLineEdit(self.dialog1)
		self.lineEdit_3.setGeometry(QtCore.QRect(50, 40, 200, 41))
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setPlaceholderText("Username...")
		self.lineEdit_3.setObjectName("lineEdit_3")
			
		self.lineEdit_4 = QtWidgets.QLineEdit(self.dialog1)
		self.lineEdit_4.setGeometry(QtCore.QRect(50, 105, 200, 41))
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setPlaceholderText("Password...")
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_4.setEchoMode(self.lineEdit_2.Password)
				
		self.lineEdit_5 = QtWidgets.QLineEdit(self.dialog1)
		self.lineEdit_5.setGeometry(QtCore.QRect(50, 170, 200, 41))
		self.lineEdit_5.setFont(font)
		self.lineEdit_5.setPlaceholderText("Confirm Password...")
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_5.setEchoMode(self.lineEdit_3.Password)
				
		self.pushButton2 = QtWidgets.QPushButton(self.dialog1)
		self.pushButton2.setGeometry(QtCore.QRect(100, 230, 100, 23))
		self.pushButton2.setObjectName("pushButton1")
		self.pushButton2.setText(QtWidgets.QApplication.translate("dialog1", "Sign Up", None, -1))
		self.pushButton2.clicked.connect(partial(self.check))
			
		self.dialog1.show()
		
	def check(self):
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(8)
		font.setWeight(10)

		username = self.lineEdit_3.text()
		password = self.lineEdit_4.text()
		confirmPassword = self.lineEdit_5.text()
		checkingUsername = True 
		checkingPassword = True 
		checkingConfirmPassword = True 
		
		con = sqlite3.connect(r'C://Users//Public//Desktop//Account.db')
		cur = con.cursor()
		cur.execute("SELECT Username FROM Account")
		temp = cur.fetchall()
		existedUsername = []
		for row_number, row_data in enumerate(temp):
			for column_number, data in enumerate(row_data):
				existedUsername.append(data)
		con.close()
		print(existedUsername)
		if(str(username).__len__() == 0):	
			self.label3 = QtWidgets.QLabel(self.dialog1)
			self.label3.setFont(font)		
			self.label3.setGeometry(QtCore.QRect(50, 20, 300, 20))
			self.label3.setText(QtWidgets.QApplication.translate("dialog1", "ERROR: Username can't be empty !!!",  None, -1))
			self.label3.show()
			
			checkingUsername = False

		if(str(username) in existedUsername):
			self.label3 = QtWidgets.QLabel(self.dialog1)
			self.label3.setFont(font)		
			self.label3.setGeometry(QtCore.QRect(50, 20, 300, 20))
			self.label3.setText(QtWidgets.QApplication.translate("dialog1", "ERROR: Username has been aldready existed !!!",  None, -1))
			self.label3.show()
			self.lineEdit_3.clear()
			self.lineEdit_4.clear()
			self.lineEdit_5.clear()
			checkingUsername = False
						
		if(str(password).__len__() < 8):
			font = QtGui.QFont()
			font.setFamily("Times New Roman")
			font.setPointSize(8)
			font.setWeight(10)
			
			if(str(password).__len__() == 0):
				self.label = QtWidgets.QLabel(self.dialog1)
				self.label.setFont(font)		
				self.label.setGeometry(QtCore.QRect(50, 85, 300, 20))
				self.label.setText(QtWidgets.QApplication.translate("dialog1", "ERROR: Password can't be empty !!!",  None, -1))
				self.label.show()

				self.lineEdit_4.clear()
				self.lineEdit_5.clear()

			else:
				self.label = QtWidgets.QLabel(self.dialog1)
				self.label.setFont(font)		
				self.label.setGeometry(QtCore.QRect(50, 85, 300, 20))
				self.label.setText(QtWidgets.QApplication.translate("dialog1", "ERROR: Password must have at least 8 character !!!",  None, -1))
				self.label.show()

				self.lineEdit_4.clear()
				self.lineEdit_5.clear()
				
			checkingPassword = False
			
		if(password != confirmPassword):
			font = QtGui.QFont()
			font.setFamily("Times New Roman")
			font.setPointSize(8)
			font.setWeight(10)
			
			self.label2 = QtWidgets.QLabel(self.dialog1)
			self.label2.setFont(font)		
			self.label2.setGeometry(QtCore.QRect(50, 150, 300, 20))
			self.label2.setText(QtWidgets.QApplication.translate("dialog1", "ERROR: Confirm Password doesn't match with Password !!!",  None, -1))
			self.label2.show()

			self.lineEdit_4.clear()
			self.lineEdit_5.clear()

			checkingConfirmPassword = False

		if(checkingConfirmPassword == True and checkingPassword == True and checkingUsername == True):

			now = datetime.now()
			dt = now.strftime("%d/%m/%Y %H:%M:%S")
			data = (username, password, dt, )
			con = sqlite3.connect('C://Users//Public//Desktop//Account.db')
			cur = con.cursor()
			cur.execute('INSERT INTO Account VALUES(?, ?, ?)', data)
			con.commit()
			con.close()

			msg = QtWidgets.QMessageBox()
			msg.setIcon(msg.Information)
			msg.setText("Sign Up Successfully!")
			msg.setWindowTitle("Notification!")
			msg.exec_()

	def signIn(self):
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(8)
		font.setWeight(10)
		checkingUsername = False
		username = self.lineEdit_1.text()
		password = self.lineEdit_2.text()
		data = (username, )
		con = sqlite3.connect('C://Users//Public//Desktop//Account.db')
		cur = con.cursor()
		cur.execute('SELECT Password FROM Account WHERE Username = ?', data)
		data = cur.fetchall()
		try:
			if(password == data[0][0]):
				print("Sign In Success")	
				Dialog.close()
				msg = QtWidgets.QMessageBox()
				msg.setIcon(msg.Information)
				msg.setText("Sign In Successfully!")
				msg.setWindowTitle("Notification!")
				msg.exec_()
				
			else:					
				self.label5 = QtWidgets.QLabel(Dialog)
				self.label5.setFont(font)
				self.label5.setGeometry(QtCore.QRect(50, 100, 300, 20))
				self.label5.setText(QtWidgets.QApplication.translate("Dialog", "ERROR: Password is incorrect !!!",  None, -1))
				self.label5.show()
				self.lineEdit_2.clear()
				

		except:
			self.label6 = QtWidgets.QLabel(Dialog)
			self.label6.setFont(font)
			self.label6.setGeometry(QtCore.QRect(50, 40, 300, 20))
			self.label6.setText(QtWidgets.QApplication.translate("Dialog", "ERROR: Username doesn't exist !!!",  None, -1))
			self.label6.show()
			self.lineEdit_1.clear()
		con.close()
app = QtWidgets.QApplication(sys.argv)		
ui = UI()
Dialog = QtWidgets.QWidget()
ui.setupUI(Dialog)
Dialog.activateWindow()
sys.exit(app.exec_())

con = sqlite3.connect('C://Users//Public//Desktop//Account.db')
cur = con.cursor()
cur.execute('SELECT * FROM Account')
data = cur.fetchall()
print(data)
con.close()

