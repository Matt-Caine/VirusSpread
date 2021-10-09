import sys
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


from PyQt5.QtGui import QPixmap

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

        # Progress bar
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.hide()

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
        # k_chance group
        self.sbx_k_chance = QtWidgets.QSpinBox(self)
        self.lbl_k_chance = QtWidgets.QLabel(self)

        # Iterations group
        self.sbx_days = QtWidgets.QSpinBox(self)
        self.lbl_days = QtWidgets.QLabel(self)
        # Infected group
        self.sbx_infected = QtWidgets.QSpinBox(self)
        self.lbl_infected = QtWidgets.QLabel(self)
        # Healthy group
        self.sbx_healthy = QtWidgets.QSpinBox(self)
        self.lbl_healthy = QtWidgets.QLabel(self)
        # Networks group
        self.lbl_networks = QtWidgets.QLabel(self)
        self.sbx_networks = QtWidgets.QSpinBox(self)

        # Header Img
        self.Head_img = QPixmap('assets/img/Header.png')
        self.header = QtWidgets.QLabel(self)

        #Me
        self.lbl_MattCaine = QtWidgets.QLabel(self)

        # Window frame settings
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Comp3000 - Computer Virus Spread Simulation")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('assets/img/Header.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        self.initUI()

    def initUI(self):

        #----------------------------------Form----------------------------------#

        self.header.setPixmap(self.Head_img)
        self.header.resize(1000, 50)

        self.lbl_MattCaine.setText("© Matt Caine - UoP - Comp3000 Project")
        self.lbl_MattCaine.setGeometry(788, 679, 300, 20)

        self.lbl_name.setText("Simulation Name")
        self.lbl_name.setGeometry(145, 70, 300, 20)

        self.inp_name.setGeometry(145, 89, 300, 29)

        # ----------------------------------Titles----------------------------------#

        self.lbl_Param_Header.setText("𝗡𝗼𝗱𝗲 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_Param_Header.move(16, 50)

        self.lbl_virus_Header.setText("𝗩𝗶𝗿𝘂𝘀 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_virus_Header.move(16, 260)

        self.lbl_simulation_Header.setText("𝗦𝗶𝗺𝘂𝗹𝗮𝘁𝗶𝗼𝗻:")
        self.lbl_simulation_Header.move(145, 50)


        #----------------------------------parameter Section----------------------------------#

        #--------Networks--------#
        self.lbl_networks.setText("Networks")
        self.lbl_networks.move(20, 65)

        self.sbx_networks.move(19, 89)
        self.sbx_networks.setMinimum(1)
        self.sbx_networks.setMaximum(99999)
        self.sbx_networks.setValue(100)
        self.sbx_networks.setSingleStep(100)

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
        self.sbx_infected.setMaximum(99999)
        self.sbx_infected.setValue(100)
        self.sbx_infected.setSingleStep(100)

        #--------Iterations--------#
        self.lbl_days.setText("Days")
        self.lbl_days.move(20, 209)

        self.sbx_days.move(19, 233)
        self.sbx_days.setMinimum(10)
        self.sbx_days.setMaximum(365)
        self.sbx_days.setValue(200)
        self.sbx_days.setSingleStep(5)

        # --------Pick a Virus--------#

        self.lbl_viruses.setText("Use existing virus")
        self.lbl_viruses.move(20, 275)

        self.cbx_viruses.addItem("Use Custom")
        self.cbx_viruses.addItems(["WannaCry", "ILOVEYOU", "CryptoLocker", "Sasser","*COVID-19"])
        self.cbx_viruses.setGeometry(19, 299, 100, 25)

        self.cbx_viruses.currentTextChanged.connect(self.on_combobox_changed)

        #self.cbx_viruses.setDisabled(True)


        # --------propagation--------#
        self.lbl_propagation.setText("Propagation (%)")
        self.lbl_propagation.move(20, 323)

        self.sbx_propagation.move(19, 347)
        self.sbx_propagation.setMinimum(1)
        self.sbx_propagation.setMaximum(100)
        self.sbx_propagation.setValue(1)
        self.sbx_propagation.setSingleStep(5)

        # --------hibernation--------#
        self.lbl_hibernation.setText("Hibernation Days")
        self.lbl_hibernation.move(20, 371)

        self.sbx_hibernation.move(19, 395)
        self.sbx_hibernation.setMinimum(1)
        self.sbx_hibernation.setMaximum(99999)
        self.sbx_hibernation.setValue(30)
        self.sbx_hibernation.setSingleStep(10)

        # --------kill_chance--------#
        self.lbl_k_chance.setText("Kill (%)")
        self.lbl_k_chance.move(20, 419)

        self.sbx_k_chance.move(19, 443)
        self.sbx_k_chance.setMinimum(1)
        self.sbx_k_chance.setMaximum(100)
        self.sbx_k_chance.setValue(40)
        self.sbx_k_chance.setSingleStep(5)


        #--------Reset Button--------#
        self.btn_reset.setText("Reset")
        self.btn_reset.move(19, 650)
        self.btn_reset.clicked.connect(self.reset_parameters)


        # ----------------------------------Simulate----------------------------------#
        self.btn_simulate.setText("Simulate")
        self.btn_simulate.move(880, 650)
        self.btn_simulate.clicked.connect(self.download_test)

        self.progress.setGeometry(4, 685, 1001, 11)


    # ----------------------------------Functions----------------------------------#
    # --------Test Button--------#
    @staticmethod
    def Click_test():
        print("Button Clicked")

    def Disable_Custom(self):
        self.lbl_propagation.setDisabled(True)
        self.lbl_hibernation.setDisabled(True)
        self.lbl_k_chance.setDisabled(True)
        self.sbx_propagation.setDisabled(True)
        self.sbx_hibernation.setDisabled(True)
        self.sbx_k_chance.setDisabled(True)

    def Enable_Custom(self):
        self.lbl_propagation.setDisabled(False)
        self.lbl_hibernation.setDisabled(False)
        self.lbl_k_chance.setDisabled(False)
        self.sbx_propagation.setDisabled(False)
        self.sbx_hibernation.setDisabled(False)
        self.sbx_k_chance.setDisabled(False)


    def on_combobox_changed(self, value):
        if value == 'WannaCry':
            self.Disable_Custom()
            self.sbx_propagation.setValue(1)
            self.sbx_hibernation.setValue(2)
            self.sbx_k_chance.setValue(3)

        elif value == 'ILOVEYOU':
            self.Disable_Custom()
            self.sbx_propagation.setValue(4)
            self.sbx_hibernation.setValue(5)
            self.sbx_k_chance.setValue(6)

        elif value == 'CryptoLocker':
            self.Disable_Custom()
            self.sbx_propagation.setValue(7)
            self.sbx_hibernation.setValue(8)
            self.sbx_k_chance.setValue(9)

        elif value == 'Sasser':
            self.Disable_Custom()
            self.sbx_propagation.setValue(10)
            self.sbx_hibernation.setValue(11)
            self.sbx_k_chance.setValue(12)

        elif value == '*COVID-19':
            self.Disable_Custom()
            self.sbx_propagation.setValue(13)
            self.sbx_hibernation.setValue(14)
            self.sbx_k_chance.setValue(15)

        else:
            self.Enable_Custom()
            self.reset_parameters()


    def download_test(self):
        self.lbl_MattCaine.hide()
        self.progress.show()
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        self.progress.hide()
        self.lbl_MattCaine.show()

    # --------Parameter Reset Button--------#
    def reset_parameters(self):
        ret = QMessageBox.question(self, 'Parameter Reset', "Are you sure? This will reset all parameters.",
                                   QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.sbx_networks.setValue(100)
            self.sbx_healthy.setValue(25000)
            self.sbx_infected.setValue(100)
            self.sbx_days.setValue(200)
            self.sbx_propagation.setValue(1)
            self.sbx_hibernation.setValue(30)
            self.sbx_k_chance.setValue(40)
            self.cbx_viruses.setCurrentIndex(0)


# ----------------------------------Window----------------------------------#
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

