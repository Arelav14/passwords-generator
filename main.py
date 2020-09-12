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
		self.ui.pushButton.clicked.connect(self.pushbutton)
		self.ui.pushButton_2.clicked.connect(self.pushbutton2)
		self.show()

	def calls(self):
			length = int(self.ui.comboBox.currentText())
			email_length = int(self.ui.comboBox_3.currentText())
			letters = ''
			email_letters = ''
			if self.ui.checkBox.isChecked() == True:
				letters = letters + string.punctuation
			if self.ui.checkBox_2.isChecked() == True:
				letters = letters + string.digits
				email_letters = email_letters + string.digits
			if self.ui.checkBox_3.isChecked() == True:
				letters = letters + string.ascii_uppercase
				email_letters = email_letters + string.ascii_uppercase
			if self.ui.checkBox_4.isChecked() == True:
				letters = letters + string.ascii_lowercase
				email_letters = email_letters + string.ascii_lowercase
			if self.ui.checkBox_5.isChecked() == True:
				choice = ''.join(random.sample(letters, length))
				choice_email = ''.join(random.sample(email_letters, email_length)) + '@gmail.com'
			else:
				choice = ''.join(random.choice(letters) for i in range(length))
				choice_email = ''.join(random.choice(email_letters) for i in range(email_length)) + '@gmail.com'
			return length, email_length, letters, email_letters

	def generate(self):
			length, email_length, letters, email_letters = self.calls()
			if self.ui.checkBox_5.isChecked() == True:
				choice = ''.join(random.sample(letters, length))
				choice_email = ''.join(random.sample(email_letters, email_length)) + '@gmail.com'
			else:
				choice = ''.join(random.choice(letters) for i in range(length))
				choice_email = ''.join(random.choice(email_letters) for i in range(email_length)) + '@gmail.com'
			return choice_email, choice

	def pushbutton(self):
		try:
			self.calls()
			self.generate()
			choice_email, choice = self.generate()
			self.ui.textEdit.setText(choice)
			self.ui.textEdit_2.setText(choice_email)
		except:
			self.ui.textEdit.setText('')
			self.ui.textEdit_2.setText('Error!')

	def pushbutton2(self):
		try:
			self.calls()
			self.generate()
			choice_email, choice = self.generate()
			passwords = int(self.ui.comboBox_2.currentText())
			txt = open('passwords.txt', 'w')
			for i in range(passwords):
				self.generate()
				txt.writelines('Account ' + str(i + 1) + ':\n' + choice_email + '\n' + choice + '\n\n')
			self.ui.textEdit.setText('')
			self.ui.textEdit_2.setText("Done! Please check program's folder!")
		except:
			self.ui.textEdit_2.setText("Error!")
			self.ui.textEdit.setText('')

application = QApplication([])
MainWindow = MainWindow()
application.setApplicationName('Password Generator')
sys.exit(application.exec_())