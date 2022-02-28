import sys
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSplashScreen, QGridLayout, QWidget, QDesktopWidget, QCheckBox
from PyQt5.QtGui import QPixmap

from models import SIR, SIRD, SIS, SEIR

class Splash(QSplashScreen):
    def __init__(self):
        super(Splash, self).__init__()

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        label = QtWidgets.QLabel(self)
        pixmap = QPixmap('Splash.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()

        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # ----------------------------------Initialize----------------------------------#

        #Run sim Button
        self.btn_simulate = QtWidgets.QPushButton(self)

        # Save sim Button
        self.btn_Save = QtWidgets.QPushButton(self)

        self.Save_msg = QMessageBox()
        self.Save_msg.setWindowTitle("Virus Spread")
        self.Save_msg.setText("Your figure has been saved to /Saved/")

        self.Not_added_msg = QMessageBox()
        self.Not_added_msg.setWindowTitle("Virus Spread")
        self.Not_added_msg.setText("Sorry, The S.E.I.R model has not been added yet 😞")

        #progress
        self.progress = QtWidgets.QProgressBar(self)

        #Param Reset button
        self.btn_reset = QtWidgets.QPushButton(self)

        #dropodown
        self.lbl_viruses = QtWidgets.QLabel(self)
        self.cbx_viruses = QtWidgets.QComboBox(self)

        # name
        self.inp_name = QtWidgets.QLineEdit(self)
        self.lbl_name = QtWidgets.QLabel(self)

        # Header
        self.lbl_Param_Header = QtWidgets.QLabel(self)
        self.lbl_virus_Header = QtWidgets.QLabel(self)
        self.lbl_simulation_Header = QtWidgets.QLabel(self)
        self.lbl_other_Header = QtWidgets.QLabel(self)

        # propagation_chance group
        self.sbx_propagation = QtWidgets.QSpinBox(self)
        self.lbl_propagation = QtWidgets.QLabel(self)

        # mortality group
        self.sbx_mortality = QtWidgets.QSpinBox(self)
        self.lbl_mortality = QtWidgets.QLabel(self)

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
        self.Head_img = QPixmap('Header.png')
        self.header = QtWidgets.QLabel(self)

        #Fig
        self.figure = QtWidgets.QLabel(self)

        #Me
        self.lbl_MattCaine = QtWidgets.QLabel(self)

        #-----------------------------------------------------------------------------------------------Other section
        self.chbx_firewall = QtWidgets.QCheckBox("IDS/IPS",self)
        self.chbx_disconnected = QtWidgets.QCheckBox("Offline Nodes", self)
        self.chbx_3 = QtWidgets.QCheckBox("Option 3", self)
        self.chbx_4 = QtWidgets.QCheckBox("Option 4", self)
        self.chbx_5 = QtWidgets.QCheckBox("Option 5", self)
        self.chbx_6 = QtWidgets.QCheckBox("Option 6", self)

        # Window frame settings
        self.setFixedSize(1700, 900)
        self.setWindowTitle("Computer Virus Spread Visualization 2022")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('Header.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)
        self.initUI()
        self.simulate()

    def initUI(self):

        #window Icon
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #----------------------------------Form----------------------------------#


        self.header.setPixmap(self.Head_img)
        self.header.resize(1920, 50)

        self.lbl_MattCaine.setText("© Matt Caine - UoP - Comp3000 Project")
        self.lbl_MattCaine.setGeometry(1490, 875, 300, 20)

        self.btn_Save.setDisabled(True)
        self.sbx_hibernation.setDisabled(True)
        self.sbx_mortality.setDisabled(True)

        # ----------------------------------Titles----------------------------------#

        self.lbl_simulation_Header.setText("𝗦𝗶𝗺𝘂𝗹𝗮𝘁𝗶𝗼𝗻:")
        self.lbl_simulation_Header.move(145, 50)

        self.lbl_Param_Header.setText("𝗚𝗹𝗼𝗯𝗮𝗹 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_Param_Header.move(16, 50)

        self.lbl_virus_Header.setText("𝗩𝗶𝗿𝘂𝘀 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_virus_Header.move(16, 260)

        self.lbl_other_Header.setText("𝗥𝗗𝗠 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:")
        self.lbl_other_Header.move(16, 470)


        #----------------------------------parameter Section----------------------------------#

        #--------Virus Model--------#
        self.lbl_Virus_Model.setText("Virus Model")
        self.lbl_Virus_Model.move(20, 65)

        self.cbx_Virus_Model.addItems(["✅ S.I.R","✅ S.I.R/D", "❌ S.E.I.R", "✅ S.I.S"])
        self.cbx_Virus_Model.setGeometry(19, 90, 100, 25)

        self.cbx_Virus_Model.currentTextChanged.connect(self.on_model_combobox_changed)

        #--------Susceptible--------#
        self.lbl_healthy.setText("Starting Susceptible")
        self.lbl_healthy.move(20, 113)

        self.sbx_healthy.move(19, 137)
        self.sbx_healthy.setMinimum(1)
        self.sbx_healthy.setMaximum(99999)
        self.sbx_healthy.setValue(25000)
        self.sbx_healthy.setSingleStep(100)

        #--------Infected--------#
        self.lbl_infected.setText("Starting Infected")
        self.lbl_infected.move(20, 161)

        self.sbx_infected.move(19, 185)
        self.sbx_infected.setMinimum(1)
        self.sbx_infected.setMaximum(99999)
        self.sbx_infected.setValue(100)
        self.sbx_infected.setSingleStep(100)

        #--------Iterations--------#
        self.lbl_days.setText("Days to Show")
        self.lbl_days.move(20, 209)

        self.sbx_days.move(19, 233)
        self.sbx_days.setMinimum(10)
        self.sbx_days.setMaximum(10000)
        self.sbx_days.setValue(365)
        self.sbx_days.setSingleStep(5)

        # --------propagation--------#
        self.lbl_propagation.setText("Propagation Rate %")
        self.lbl_propagation.move(20, 275)
        self.sbx_propagation.move(19, 299)

        self.sbx_propagation.setMinimum(1)
        self.sbx_propagation.setMaximum(100)
        self.sbx_propagation.setValue(5)
        self.sbx_propagation.setSingleStep(5)

        # --------hibernation--------#
        self.lbl_hibernation.setText("Hibernation Days")
        self.lbl_hibernation.move(20, 323)
        self.sbx_hibernation.move(19, 347)

        self.sbx_hibernation.setMinimum(1)
        self.sbx_hibernation.setMaximum(99999)
        self.sbx_hibernation.setValue(0)
        self.sbx_hibernation.setSingleStep(10)

        # --------r_chance--------#
        self.lbl_r_chance.setText("Recovery Rate %")
        self.lbl_r_chance.move(20, 371)
        self.sbx_r_chance.move(19, 395)

        self.sbx_r_chance.setMinimum(1)
        self.sbx_r_chance.setMaximum(100)
        self.sbx_r_chance.setValue(10)
        self.sbx_r_chance.setSingleStep(5)


        # --------Mortality--------#
        self.lbl_mortality.setText("Mortality Rate %")
        self.lbl_mortality.move(20, 419)
        self.sbx_mortality.move(19, 443)

        self.sbx_mortality.setMinimum(1)
        self.sbx_mortality.setMaximum(100)
        self.sbx_mortality.setValue(5)
        self.sbx_mortality.setSingleStep(5)

        # ----------------------------------other Section----------------------------------#


        self.chbx_firewall.move(19, 490)
        self.chbx_disconnected.move(19, 510)

        self.chbx_3.move(19, 530)
        self.chbx_4.move(19, 550)
        self.chbx_5.move(19, 570)
        self.chbx_6.move(19, 590)


        # ----------------------------------SIMSection----------------------------------#

        #--------Reset Button--------#
        self.btn_reset.setText("🗑️ Reset")
        self.btn_reset.move(19, 769)
        self.btn_reset.clicked.connect(self.reset_parameters)

        # ----------------------------------Simulate----------------------------------#
        self.btn_simulate.setText("📈 Simulate")

        self.btn_simulate.move(19, 841)

        self.btn_simulate.clicked.connect(self.simulate)

        # ----------------------------------Simulate----------------------------------#

        self.btn_Save.setText("💾 Save Figure")
        self.btn_Save.move(19, 805)

        self.btn_Save.clicked.connect(self.Save)


    # ----------------------------------Functions----------------------------------#
    # --------Test Button--------#
    @staticmethod
    def Click_test():
        print("Button Clicked")

    # --------Save--------#

    def Save(self):
        self.img = QPixmap('fig_temp.png')

        self.img.save('Saved/{stamp}.png'.format(stamp = time.strftime("%Y%m%d-%H%M%S")))
        self.Save_msg.exec_()


    # --------model locks--------#
    def on_model_combobox_changed(self, value):
        if "E" in value:
            self.sbx_hibernation.setDisabled(False)
            self.sbx_mortality.setDisabled(True)
        elif "D" in value:
            self.sbx_hibernation.setDisabled(True)
            self.sbx_mortality.setDisabled(False)
        else:
            self.sbx_hibernation.setDisabled(True)
            self.sbx_mortality.setDisabled(True)

    # --------Parameter Reset Button--------#
    def reset_parameters(self):
        ret = QMessageBox.question(self, 'Parameter Reset', "Are you sure? This will reset all parameters.",
                                   QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.cbx_Virus_Model.setCurrentIndex(0)
            self.sbx_healthy.setValue(25000)
            self.sbx_infected.setValue(100)
            self.sbx_days.setValue(365)
            self.sbx_propagation.setValue(5)
            self.sbx_hibernation.setValue(1)
            self.sbx_r_chance.setValue(10)
            self.cbx_viruses.setCurrentIndex(0)
            self.sbx_mortality.setValue(5)
            self.simulate()
            self.chbx_disconnected.setChecked(False)
            self.chbx_firewall.setChecked(False)

    # -----------------------------------------------------MODELS-----------------------------------------------------#

    def simulate(self):
        try:

            if self.cbx_Virus_Model.currentIndex() == 0:
                SIR(self.sbx_healthy, self.sbx_infected, self.sbx_days, self.sbx_propagation, self.sbx_r_chance, self.chbx_firewall, self.chbx_disconnected)


                print("SIR_Simulation()")
                #show results
                self.Fig_img = QPixmap('fig_temp.png')
                self.figure.setPixmap(self.Fig_img)
                self.figure.resize(self.Fig_img.width(), self.Fig_img.height())
                self.figure.move(145, 80)

                self.btn_Save.setDisabled(False)

            elif self.cbx_Virus_Model.currentIndex() == 1:
                SIRD(self.sbx_healthy, self.sbx_infected, self.sbx_days, self.sbx_propagation, self.sbx_r_chance,self.sbx_mortality,self.chbx_firewall, self.chbx_disconnected)

                print("SIRD_Simulation()")
                #show results
                self.Fig_img = QPixmap('fig_temp.png')
                self.figure.setPixmap(self.Fig_img)
                self.figure.resize(self.Fig_img.width(), self.Fig_img.height())
                self.figure.move(145, 80)

                self.btn_Save.setDisabled(False)

            elif self.cbx_Virus_Model.currentIndex() == 2:
                SEIR(self.sbx_healthy, self.sbx_infected, self.sbx_days,self.sbx_hibernation, self.sbx_propagation, self.sbx_r_chance, self.chbx_firewall, self.chbx_disconnected)

                print("SEIR_Simulation()")
                #show results
                self.Fig_img = QPixmap('fig_temp.png')
                self.figure.setPixmap(self.Fig_img)
                self.figure.resize(self.Fig_img.width(), self.Fig_img.height())
                self.figure.move(145, 80)

                self.btn_Save.setDisabled(False)


            elif self.cbx_Virus_Model.currentIndex() == 3:
                SIS(self.sbx_healthy, self.sbx_infected, self.sbx_days, self.sbx_propagation, self.sbx_r_chance,self.chbx_firewall,self.chbx_disconnected)

                print("SIS_Simulation()")
                # show results
                self.Fig_img = QPixmap('fig_temp.png')
                self.figure.setPixmap(self.Fig_img)
                self.figure.resize(self.Fig_img.width(), self.Fig_img.height())
                self.figure.move(145, 80)

                self.btn_Save.setDisabled(False)

        except Exception as e: print(e)


# ----------------------------------Window----------------------------------#
def window():
    app = QApplication(sys.argv)
    splash = Splash()
    win = MyWindow()
    splash.show()
    print("Spalsh()")
    time.sleep(0.8)
    splash.hide()
    print("Main_Win_Show()")
    win.show()
    sys.exit(app.exec_())

window()

