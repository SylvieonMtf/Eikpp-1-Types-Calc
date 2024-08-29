
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDir, QFileInfo
import os

class Ui_Form(object):
    def __init__(self):
        self.effectiveness_chart = {
        'fighting': {'grass': 0.5, 'steel': 0, 'rock': 0.5}, 
        'ground': {'ground': 0.5, 'ice': 0.5, 'fire': 2, 'normal': 2, 'poison': 2, 'grass': 0.5, 'psychic': 0.5, 'rock': 2}, 
        'ice': {'ground': 2, 'ice': 0.5, 'fire': 0.5, 'electric': 2, 'grass': 2, 'psychic': 0.5}, 
        'fairy': {'ice': 2, 'fairy': 0.5, 'fire': 0.5, 'electric': 0, 'dragon': 2, 'psychic': 0.5}, 
        'fire': {'ground': 0.5, 'ice': 2, 'fire': 0.5, 'flying': 0.5, 'electric': 2, 'dragon': 0.5, 'poison': 0.5, 'grass': 2, 'psychic': 0.5, 'rock': 0.5}, 
        'normal': {'ground': 0.5, 'ice': 0.5, 'fire': 2, 'normal': 0.5, 'electric':2, 'dragon': 2, 'psychic': 2, 'rock': 0.5}, 
        'dark': {'fighting': 2, 'normal': 2, 'flying': 0.5, 'dragon': 0.5, 'ghost': 0.5, 'poison': 0.5, 'grass': 2, 'steel': 0, 'bug': 2, 'rock': 2, 'water': 0.5}, 
        'flying': {'fire': 2, 'flying': 0.5, 'electric': 0.5, 'grass': 0.5, 'steel': 0.5, 'rock': 0, 'water': 2}, 
        'electric': {'ground': 2, 'fairy': 2, 'fire': 0.5, 'flying': 2, 'dragon': 0, 'poison': 0.5, 'grass': 2, 'rock': 2}, 
        'dragon': {'fairy': 0.5, 'fire': 2, 'dark': 2, 'poison': 2, 'grass': 0.5, 'rock': 0.5}, 
        'ghost': {'dark': 2, 'flying': 2, 'ghost': 0.5, 'bug': 0, 'rock': 0.5}, 
        'poison': {'ground': 0.5, 'fire': 2, 'dark': 0.5, 'flying': 0.5, 'dragon': 0.5, 'ghost': 2, 'steel': 0.5, 'bug': 2, 'rock': 0.5, 'water': 0.5}, 
        'grass': {'ground': 2, 'normal': 2, 'dark': 0.5, 'electric': 0.5, 'dragon': 2, 'poison': 2, 'rock': 0.5}, 
        'steel': {'fighting': 0, 'ghost': 2, 'steel': 2, 'bug': 0.5}, 
        'psychic': {'psychic': 2, 'rock': 0.5, 'water': 0},
        'bug': {'dark': 0.5, 'ghost': 2, 'steel': 2, 'bug': 0.5, 'water': 0.5},
        'rock': {'ground': 0.5, 'ice': 0.5, 'fairy': 0.5, 'normal': 2, 'grass': 2, 'rock': 0.5, 'water': 2},
        'water': {'ground': 0.5, 'dark': 2, 'flying': 0.5, 'psychic': 2, 'bug': 2, 'rock': 0.5}
        }
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 260)
        Form.setStyleSheet("background-color: #F5A9B8")
        self.types_label = QtWidgets.QLabel(Form)
        self.types_label.setGeometry(QtCore.QRect(50, 25, 100, 25))
        self.types_label.setObjectName("types_label")
        self.type1_comboBox = QtWidgets.QComboBox(Form)
        self.type1_comboBox.setGeometry(QtCore.QRect(50, 50, 100, 25))
        self.type1_comboBox.setStyleSheet("background-color: white\n"
"")
        self.type1_comboBox.setObjectName("type1_comboBox")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type1_comboBox.addItem("")
        self.type2_comboBox = QtWidgets.QComboBox(Form)
        self.type2_comboBox.setGeometry(QtCore.QRect(50, 100, 100, 25))
        self.type2_comboBox.setStyleSheet("background-color: white\n"
"")
        self.type2_comboBox.setObjectName("type2_comboBox")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.type2_comboBox.addItem("")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(325, 25, 164, 164))
        image_path = self.get_image_path('sylvietrainer.png')
        self.image_label.setStyleSheet(f"""
        QWidget {{
                background-image: url('{image_path}');
                background-repeat: no-repeat;
                background-position: center;
        }}
        """)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.calculate_pushButton = QtWidgets.QPushButton(Form)
        self.calculate_pushButton.setGeometry(QtCore.QRect(50, 145, 100, 25))
        self.calculate_pushButton.setStyleSheet("background-color: white\n"
"")
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.resistance_textEdit = QtWidgets.QTextEdit(Form)
        self.resistance_textEdit.setGeometry(QtCore.QRect(175, 25, 150, 100))
        self.resistance_textEdit.setStyleSheet("background-color: white")
        self.resistance_textEdit.setObjectName("resistance_textEdit")
        self.resistance_textEdit.setReadOnly(True)
        self.weakness_textEdit = QtWidgets.QTextEdit(Form)
        self.weakness_textEdit.setGeometry(QtCore.QRect(175, 145, 150, 100))
        self.weakness_textEdit.setStyleSheet("background-color: white")
        self.weakness_textEdit.setObjectName("weakness_textEdit")
        self.weakness_textEdit.setReadOnly(True)
        self.resistance_label = QtWidgets.QLabel(Form)
        self.resistance_label.setGeometry(QtCore.QRect(175, 5, 100, 20))
        self.resistance_label.setObjectName("resistance_label")
        self.weakness_label = QtWidgets.QLabel(Form)
        self.weakness_label.setGeometry(QtCore.QRect(175, 125, 100, 20))
        self.weakness_label.setObjectName("weakness_label")
        self.color_lineEdit = QtWidgets.QLineEdit(Form)
        self.color_lineEdit.setGeometry(QtCore.QRect(360, 190, 100, 20))
        self.color_lineEdit.setStyleSheet("background-color: white")
        self.color_lineEdit.setObjectName("color_lineEdit")
        self.color_pushButton = QtWidgets.QPushButton(Form)
        self.color_pushButton.setGeometry(QtCore.QRect(360, 215, 100, 25))
        self.color_pushButton.setStyleSheet("background-color: white")
        self.color_pushButton.setObjectName("color_pushButton")

        self.calculate_pushButton.clicked.connect(self.calculate)
        self.color_pushButton.clicked.connect(self.colorchange)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eikpp-1 Type Calc"))
        self.types_label.setText(_translate("Form", "Types"))
        self.type1_comboBox.setItemText(0, _translate("Form", "(None)"))
        self.type1_comboBox.setItemText(1, _translate("Form", "Fighting"))
        self.type1_comboBox.setItemText(2, _translate("Form", "Ground"))
        self.type1_comboBox.setItemText(3, _translate("Form", "Ice"))
        self.type1_comboBox.setItemText(4, _translate("Form", "Fairy"))
        self.type1_comboBox.setItemText(5, _translate("Form", "Fire"))
        self.type1_comboBox.setItemText(6, _translate("Form", "Normal"))
        self.type1_comboBox.setItemText(7, _translate("Form", "Dark"))
        self.type1_comboBox.setItemText(8, _translate("Form", "Flying"))
        self.type1_comboBox.setItemText(9, _translate("Form", "Electric"))
        self.type1_comboBox.setItemText(10, _translate("Form", "Dragon"))
        self.type1_comboBox.setItemText(11, _translate("Form", "Ghost"))
        self.type1_comboBox.setItemText(12, _translate("Form", "Poison"))
        self.type1_comboBox.setItemText(13, _translate("Form", "Grass"))
        self.type1_comboBox.setItemText(14, _translate("Form", "Steel"))
        self.type1_comboBox.setItemText(15, _translate("Form", "Psychic"))
        self.type1_comboBox.setItemText(16, _translate("Form", "Bug"))
        self.type1_comboBox.setItemText(17, _translate("Form", "Rock"))
        self.type1_comboBox.setItemText(18, _translate("Form", "Water"))
        self.type2_comboBox.setItemText(0, _translate("Form", "(None)"))
        self.type2_comboBox.setItemText(1, _translate("Form", "Fighting"))
        self.type2_comboBox.setItemText(2, _translate("Form", "Ground"))
        self.type2_comboBox.setItemText(3, _translate("Form", "Ice"))
        self.type2_comboBox.setItemText(4, _translate("Form", "Fairy"))
        self.type2_comboBox.setItemText(5, _translate("Form", "Fire"))
        self.type2_comboBox.setItemText(6, _translate("Form", "Normal"))
        self.type2_comboBox.setItemText(7, _translate("Form", "Dark"))
        self.type2_comboBox.setItemText(8, _translate("Form", "Flying"))
        self.type2_comboBox.setItemText(9, _translate("Form", "Electric"))
        self.type2_comboBox.setItemText(10, _translate("Form", "Dragon"))
        self.type2_comboBox.setItemText(11, _translate("Form", "Ghost"))
        self.type2_comboBox.setItemText(12, _translate("Form", "Poison"))
        self.type2_comboBox.setItemText(13, _translate("Form", "Grass"))
        self.type2_comboBox.setItemText(14, _translate("Form", "Steel"))
        self.type2_comboBox.setItemText(15, _translate("Form", "Psychic"))
        self.type2_comboBox.setItemText(16, _translate("Form", "Bug"))
        self.type2_comboBox.setItemText(17, _translate("Form", "Rock"))
        self.type2_comboBox.setItemText(18, _translate("Form", "Water"))
        self.calculate_pushButton.setText(_translate("Form", "Calculate"))
        self.resistance_label.setText(_translate("Form", "Resistances"))
        self.weakness_label.setText(_translate("Form", "Weaknesses"))
        self.color_lineEdit.setText(_translate("Form", "#F5A9B8"))
        self.color_pushButton.setText(_translate("Form", "Change Colors!"))

    def get_image_path(self, image_filename):
        ui_file_path = QFileInfo(__file__).absolutePath()
        image_path = QDir(ui_file_path).filePath(image_filename)
        return image_path
    
    def calculate(self):
        type1 = self.type1_comboBox.currentText().lower()
        type2 = self.type2_comboBox.currentText().lower() if self.type2_comboBox.currentIndex() != 0 else None

        resistances = []
        weaknesses = []

        for move_type in self.effectiveness_chart.keys():
                effectiveness = self.get_effectiveness(move_type, type1, type2)

                if effectiveness in [0.00, 0.25, 0.50]:
                        resistances.append(f"{move_type}: {effectiveness:.2f}")
                elif effectiveness in [2.00, 4.00]:
                        weaknesses.append(f"{move_type}: {effectiveness:.2f}")

        self.resistance_textEdit.setText('\n'.join(resistances))
        self.weakness_textEdit.setText('\n'.join(weaknesses))

    def get_effectiveness(self, move_type, type1, type2=None):
        

        if type1 == "(None)":
                type1 = None
        if type2 == "(None)":
                type2 = None

        effectiveness = 1.0

        if move_type in self.effectiveness_chart:
                type_effectiveness = self.effectiveness_chart[move_type]
        
                if type1 in type_effectiveness:
                        effectiveness *= type_effectiveness[type1]
        
                if type2 and type2 != type1 and type2 in type_effectiveness:
                        effectiveness *= type_effectiveness[type2]

        return effectiveness
    
    def colorchange(self):
        try:
                hex_color = self.color_lineEdit.text()
                if not hex_color.startswith('#') or len(hex_color) != 7:
                        raise ValueError("Invalid Hex Code")
                self.setStyleSheet(f"background-color: {hex_color};")
        except ValueError as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error: Invalid Hex Code")
                msg.setInformativeText("Please enter a valid hex color code (e.g., #FFFFFF).")
                msg.setWindowTitle("Invalid Input")
                msg.exec_()
                self.color_lineEdit.setText("#F5A9B8")
                self.setStyleSheet("background-color: #F5A9B8;")