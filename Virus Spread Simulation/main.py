import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from models import SIR


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # ----------------------------------Initialize----------------------------------#
        #Run Button
        self.completed = 0
        self.btn_simulate = QtWidgets.QPushButton(self)
        #Param Reset button
        self.btn_reset = QtWidgets.QPushButton(self)

        #dropodown
        self.lbl_viruses = QtWidgets.QLabel(self)
        self.cbx_viruses = QtWidgets.QComboBox(self)

        # name
        self.inp_name = QtWidgets.QLineEdit(self)
        self.lbl_name = QtWidgets.QLabel(self)

        # Headers
        self.lbl_Param_Header = QtWidgets.QLabel(self)
        self.lbl_virus_Header = QtWidgets.QLabel(self)
        self.lbl_simulation_Header = QtWidgets.QLabel(self)

        # propagation_chance group
        self.sbx_propagation = QtWidgets.QSpinBox(self)
        self.lbl_propagation = QtWidgets.QLabel(self)
        # hibernation_Days group
        self.sbx_hibernation = QtWidgets.QSpinBox(self)
        self.lbl_hibernation = QtWidgets.QLabel(self)
        # r_chance group
        self.sbx_r_chance = QtWidgets.QSpinBox(self)
        self.lbl_r_chance = QtWidgets.QLabel(self)

        # Iterations group
        self.sbx_days = QtWidgets.QSpinBox(self)
        self.lbl_days = QtWidgets.QLabel(self)
        # Infected group
        self.sbx_infected = QtWidgets.QSpinBox(self)
        self.lbl_infected = QtWidgets.QLabel(self)
        # Healthy group
        self.sbx_healthy = QtWidgets.QSpinBox(self)
        self.lbl_healthy = QtWidgets.QLabel(self)

        # Virus Model
        self.lbl_Virus_Model = QtWidgets.QLabel(self)
        self.cbx_Virus_Model = QtWidgets.QComboBox(self)

        # Header Img
        self.Head_img = QPixmap('assets/img/Header.png')
        self.header = QtWidgets.QLabel(self)

        #Me
        self.lbl_MattCaine = QtWidgets.QLabel(self)

        # Window frame settings
        self.setFixedSize(1700, 900)
        self.setWindowTitle("Comp3000 - Computer Virus Spread Simulation")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('assets/img/Header.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        self.initUI()

    def initUI(self):

        #----------------------------------Form----------------------------------#

        self.header.setPixmap(self.Head_img)
        self.header.resize(1920, 50)

        self.lbl_MattCaine.setText("© Matt Caine - UoP - Comp3000 Project")
        self.lbl_MattCaine.setGeometry(1490, 875, 300, 20)


        self.sbx_hibernation.setDisabled(True)

        # ----------------------------------Titles----------------------------------#

        self.lbl_Param_Header.setText("𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_Param_Header.move(16, 50)

        self.lbl_virus_Header.setText("𝗩𝗶𝗿𝘂𝘀 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_virus_Header.move(16, 260)

        self.lbl_simulation_Header.setText("𝗦𝗶𝗺𝘂𝗹𝗮𝘁𝗶𝗼𝗻:")
        self.lbl_simulation_Header.move(145, 50)


        #----------------------------------parameter Section----------------------------------#

        #--------Virus Model--------#
        self.lbl_Virus_Model.setText("Virus Model")
        self.lbl_Virus_Model.move(20, 65)

        self.cbx_Virus_Model.addItem("✅ S.I.R")
        self.cbx_Virus_Model.addItems(["❌ S.I.R/D", "❌ S.E.I.R", "❌ S.E.I.R/D", "❌ S.I.S"])
        self.cbx_Virus_Model.setGeometry(19, 90, 100, 25)

        self.cbx_Virus_Model.currentTextChanged.connect(self.on_model_combobox_changed)

        #--------Healthy--------#
        self.lbl_healthy.setText("Healthy")
        self.lbl_healthy.move(20, 113)

        self.sbx_healthy.move(19, 137)
        self.sbx_healthy.setMinimum(1)
        self.sbx_healthy.setMaximum(99999)
        self.sbx_healthy.setValue(25000)
        self.sbx_healthy.setSingleStep(100)

        #--------Infected--------#
        self.lbl_infected.setText("Infected")
        self.lbl_infected.move(20, 161)

        self.sbx_infected.move(19, 185)
        self.sbx_infected.setMinimum(1)
        self.sbx_infected.setMaximum(self.sbx_healthy.value())
        self.sbx_infected.setValue(100)
        self.sbx_infected.setSingleStep(100)

        #--------Iterations--------#
        self.lbl_days.setText("Days")
        self.lbl_days.move(20, 209)

        self.sbx_days.move(19, 233)
        self.sbx_days.setMinimum(10)
        self.sbx_days.setMaximum(1000)
        self.sbx_days.setValue(200)
        self.sbx_days.setSingleStep(5)

        # --------Pick a Virus--------#

        self.lbl_viruses.setText("Use existing virus")
        self.lbl_viruses.move(20, 275)

        self.cbx_viruses.addItem("❌ Use Custom")
        self.cbx_viruses.addItems(["WannaCry", "ILOVEYOU", "CryptoLocker", "Sasser","*COVID-19"])
        self.cbx_viruses.setGeometry(19, 299, 100, 25)

        #self.cbx_viruses.currentTextChanged.connect(self.on_combobox_changed)

        self.cbx_viruses.setDisabled(True)


        # --------propagation--------#
        self.lbl_propagation.setText("Propagation Rate %")
        self.lbl_propagation.move(20, 323)

        self.sbx_propagation.move(19, 347)
        self.sbx_propagation.setMinimum(1)
        self.sbx_propagation.setMaximum(100)
        self.sbx_propagation.setValue(20)
        self.sbx_propagation.setSingleStep(5)

        # --------hibernation--------#
        self.lbl_hibernation.setText("Hibernation Days")
        self.lbl_hibernation.move(20, 371)

        self.sbx_hibernation.move(19, 395)
        self.sbx_hibernation.setMinimum(1)
        self.sbx_hibernation.setMaximum(99999)
        self.sbx_hibernation.setValue(0)
        self.sbx_hibernation.setSingleStep(10)

        # --------r_chance--------#
        self.lbl_r_chance.setText("Recovery Rate %")
        self.lbl_r_chance.move(20, 419)

        self.sbx_r_chance.move(19, 443)
        self.sbx_r_chance.setMinimum(1)
        self.sbx_r_chance.setMaximum(100)
        self.sbx_r_chance.setValue(10)
        self.sbx_r_chance.setSingleStep(5)


        #--------Reset Button--------#
        self.btn_reset.setText("Reset")
        self.btn_reset.move(19, 650)
        self.btn_reset.clicked.connect(self.reset_parameters)


        # ----------------------------------Simulate----------------------------------#
        self.btn_simulate.setText("Simulate")
        self.btn_simulate.move(19, 690)

        self.btn_simulate.clicked.connect(self.simulate)



    # ----------------------------------Functions----------------------------------#
    # --------Test Button--------#
    @staticmethod
    def Click_test():
        print("Button Clicked")

    def on_model_combobox_changed(self, value):
        if "E" in value:
            self.sbx_hibernation.setDisabled(False)
        else:
            self.sbx_hibernation.setDisabled(True)

    # --------Parameter Reset Button--------#
    def reset_parameters(self):
        ret = QMessageBox.question(self, 'Parameter Reset', "Are you sure? This will reset all parameters.",
                                   QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.cbx_Virus_Model.setCurrentIndex(0)
            self.sbx_healthy.setValue(25000)
            self.sbx_infected.setValue(100)
            self.sbx_days.setValue(200)
            self.sbx_propagation.setValue(20)
            self.sbx_hibernation.setValue(1)
            self.sbx_r_chance.setValue(10)
            self.cbx_viruses.setCurrentIndex(0)

    # -----------------------------------------------------MODELS-----------------------------------------------------#


    def simulate(self):
        try:
            if self.cbx_Virus_Model.currentIndex() == 0:
                SIR(self.sbx_healthy, self.sbx_infected, self.sbx_days, self.sbx_propagation, self.sbx_r_chance)

            elif self.cbx_Virus_Model.currentIndex() == 1:
                    print("S.I.R/D")

            elif self.cbx_Virus_Model.currentIndex() == 2:
                    print("S.E.I.R")

            elif self.cbx_Virus_Model.currentIndex() == 3:
                    print("S.E.I.R/D")

            elif self.cbx_Virus_Model.currentIndex() == 4:
                    print("S.I.S")
        except  ValueError:
            print(ValueError)



# ----------------------------------Window----------------------------------#
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

