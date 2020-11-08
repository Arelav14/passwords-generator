from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import Qt
import sys
import string
import random
import os
from passgenui import Ui_MainWindow

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.generatebutton)
		self.ui.pushButton_2.clicked.connect(self.outputbutton)
		self.show()

	def generate(self):
		letters = ''
		email_letters = ''
		
		if self.ui.checkBox.isChecked() == True:
			letters = letters + string.punctuation
		if self.ui.checkBox_2.isChecked() == True:
			letters, email_letters = letters + string.digits, email_letters + string.digits
		if self.ui.checkBox_3.isChecked() == True:
			letters, email_letters = letters + string.ascii_uppercase, email_letters + string.ascii_lowercase
		if self.ui.checkBox_4.isChecked() == True:
			letters, email_letters = letters + string.ascii_lowercase, email_letters + string.ascii_lowercase

		postfix = self.ui.textEdit_4.toPlainText()
		length = int(self.ui.comboBox.currentText())
		email_length = int(self.ui.comboBox_3.currentText())

		if self.ui.checkBox_5.isChecked() == True:
			choice = ''.join(random.sample(letters, length))
			choice_email = ''.join(random.sample(email_letters, email_length)) + postfix
		else:
			choice = ''.join(random.choice(letters) for i in range(length))
			choice_email = ''.join(random.choice(email_letters) for i in range(email_length)) + postfix
			
		return choice_email, choice

	def generatebutton(self):
		try:
			choice_email, choice = self.generate()
			self.ui.textEdit.setText(choice)
			self.ui.textEdit_2.setText(choice_email)
		except IndexError:
			self.ui.label_8.setText("Error! Select at least one setting for both fields!")

	def outputbutton(self):
		quantity = int(self.ui.textEdit_3.toPlainText())
		try:
			txt = open('passwords.txt', 'w')
			for i in range(quantity):
				choice_email, choice = self.generate()
				txt.writelines(f'Account {str(i + 1)}:\n{choice_email}\n{choice}')
				if (i != quantity - 1):
					txt.write('\n\n')
			self.ui.label_8.setText("Done! Please check program's folder!")
		except ValueError:
			self.ui.label_8.setText("Error! Quantity must be integer value!")
		except IndexError:
			self.ui.label_8.setText("Error! Select at least one setting for both fields!")

application = QApplication([])
MainWindow = MainWindow()
application.setApplicationName('Password Generator')
sys.exit(application.exec_())