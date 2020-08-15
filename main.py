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

	def pushbutton(self):
		try:
			length = int(self.ui.comboBox.currentText())
			letters = ''
			if self.ui.checkBox.isChecked() == True:
				box_a = string.punctuation
				letters = letters + box_a
			if self.ui.checkBox_2.isChecked() == True:
				box_b = string.digits
				letters = letters + box_b
			if self.ui.checkBox_3.isChecked() == True:
				box_c = string.ascii_uppercase
				letters = letters + box_c
			if self.ui.checkBox_4.isChecked() == True:
				box_d = string.ascii_lowercase
				letters = letters + box_d
			if self.ui.checkBox_5.isChecked() == True:
				choice = ''.join(random.sample(letters, length))
			else:
				choice = ''.join(random.choice(letters) for i in range(length))
			self.ui.textEdit.setText(choice)
		except:
			self.ui.textEdit.setText('Error! Please choose at least one chars option!')
	def pushbutton2(self):
		try:
			length = int(self.ui.comboBox.currentText())
			letters = ''
			if self.ui.checkBox.isChecked() == True:
				box_a = string.punctuation
				letters = letters + box_a
			if self.ui.checkBox_2.isChecked() == True:
				box_b = string.digits
				letters = letters + box_b
			if self.ui.checkBox_3.isChecked() == True:
				box_c = string.ascii_uppercase
				letters = letters + box_c
			if self.ui.checkBox_4.isChecked() == True:
				box_d = string.ascii_lowercase
				letters = letters + box_d
			passwords = int(self.ui.comboBox_2.currentText())
			txt = open('passwords.txt', 'w')
			for i in range(passwords):
				if self.ui.checkBox_5.isChecked() == True:
					choice = ''.join(random.sample(letters, length))
				else:
					choice = ''.join(random.choice(letters) for i in range(length))
				txt.writelines(choice + '\n')
			self.ui.textEdit.setText("Done! Please check program's folder!")
		except:
			self.ui.textEdit.setText('Error! Please choose at least one chars option!')

application = QApplication([])
MainWindow = MainWindow()
application.setApplicationName('Password Generator')
sys.exit(application.exec_())