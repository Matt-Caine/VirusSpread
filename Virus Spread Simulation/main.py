import sys
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSplashScreen, QDesktopWidget
from PyQt5.QtGui import QPixmap
import os
import uuid

from models import SIR, SIRD, SIS

class Splash(QSplashScreen):
    def __init__(self):
        super(Splash, self).__init__()
        # Window--------------------------------------------------------#
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # Splash Image--------------------------------------------------#
        label = QtWidgets.QLabel(self)
        pixmap = QPixmap('Splash.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        # Centre Window-------------------------------------------------#
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # Console Out--------------------------------------------------#
        print("[Splash]")


        # END----------------------------------------------------------#

class Disclaimer(QMainWindow):
    def __init__(self):
        super(Disclaimer, self).__init__()
        # MSG BOX--------------------------------------------------------#
        self.disclaimer = QMessageBox()
        self.disclaimer.setIcon(QMessageBox.Warning)

        self.disclaimer.setWindowIcon(QtGui.QIcon('Icon.ico'))

        # Default Answers-------------------------------------------------#
        self.disclaimer.setDefaultButton(self.disclaimer.Yes)
        self.disclaimer.setEscapeButton(self.disclaimer.Abort)

        # Console Out 1 --------------------------------------------------#
        print("[Disclaimer]")

        # MSG BOX Set - ---------------------------------------------------#
        disclaimer_answer = self.disclaimer.question(self, "Computer Virus Spread Visualization Tool Disclaimer",
                                                     "𝗗𝗶𝘀𝗰𝗹𝗮𝗶𝗺𝗲𝗿:\nThe developer of Computer Virus Spread Visualization Tool cannot be held responsible for your use of the information provided. "
                                                     "This tool should only be used as an estimate and should not be considered 100% accurate. "
                                                     "\n\n𝗗𝗼 𝘆𝗼𝘂 𝘂𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱? \n",
                                                     self.disclaimer.Yes | self.disclaimer.Abort)

        # Answer + Console Out 2 -----------------------------------------#
        if disclaimer_answer == self.disclaimer.Abort:
            print(" - Disclaimer Abort\n[Quit]")
            #quit()
            sys.exit()
        else:
            print(" - Disclaimer OK")

        # END------------------------------------------------------------#

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # Widgets ----------------------------------------------------------------#
        # Sim Button
        self.btn_simulate = QtWidgets.QPushButton("📈 | Simulate",self)

        # Pin Button
        self.btn_pin = QtWidgets.QPushButton("📌",self)

        # Folder Button
        self.btn_folder = QtWidgets.QPushButton("📁", self)

        # Model Info Button
        self.btn_Info = QtWidgets.QPushButton("❓", self)
        self.btn_Info.hide()

        # Undo Button
        self.btn_undo = QtWidgets.QPushButton("🔙", self)

        # Save Button
        self.btn_Save = QtWidgets.QPushButton("💾 | Save", self)

        #WaterMark
        self.WaterMark_img = QPixmap('LogoWaterMark.png')
        self.WaterMark = QtWidgets.QLabel(self)

        # Save msg Box
        self.Save_msg = QMessageBox()
        self.Save_msg.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.Save_msg.setWindowTitle("Computer Virus Spread Visualization Tool")

        # Gen use Msg box
        self.msg_box = QMessageBox()
        self.msg_box.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.msg_box.setWindowTitle("Computer Virus Spread Visualization Tool")

        # Progress bar
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(2, 878, 1698, 16)
        Bar_STYLE = """
        QProgressBar{
            border: 2px solid grey;
            border-radius: 5px;
            bar.setFormat("% p")
            text-align: center
        }
        QProgressBar::chunk {
            background-color: #2CA02C;
            width: 10px;
            margin: 1px;
        }
        """
        self.progress.setStyleSheet(Bar_STYLE)
        self.progress.hide()

        #sim name lbl
        self.lbl_sim_name = QtWidgets.QLabel(self)

        #Param Reset button
        self.btn_reset = QtWidgets.QPushButton("🗑️ | Reset All",self)

        #dropodown
        self.cbx_viruses = QtWidgets.QComboBox(self)

        # Headers
        self.lbl_Param_Header = QtWidgets.QLabel("𝗚𝗹𝗼𝗯𝗮𝗹 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:",self)
        self.lbl_virus_Header = QtWidgets.QLabel("𝗩𝗶𝗿𝘂𝘀 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀:",self)
        self.lbl_simulation_Header = QtWidgets.QLabel("𝗦𝗶𝗺𝘂𝗹𝗮𝘁𝗶𝗼𝗻 𝗜𝗗:",self)
        self.lbl_other_Header = QtWidgets.QLabel("𝗠𝗶𝘀𝗰. 𝗠𝗼𝗱𝗶𝗳𝗶𝗲𝗿𝘀:",self)
        self.lbl_actions_Header = QtWidgets.QLabel("𝗔𝗰𝘁𝗶𝗼𝗻 𝗕𝘂𝘁𝘁𝗼𝗻𝘀:",self)

        self.lbl_simulation_Header.move(145, 50)
        self.lbl_Param_Header.move(15, 50)
        self.lbl_virus_Header.move(15, 260)
        self.lbl_other_Header.move(15, 470)
        self.lbl_actions_Header.move(15, 740)
        self.lbl_sim_name.move(220, 50)

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
        self.lbl_Virus_Model = QtWidgets.QLabel("Virus Model",self)
        self.cbx_Virus_Model = QtWidgets.QComboBox(self)

        # Header Img
        self.Head_img = QPixmap('Header.png')
        self.header = QtWidgets.QLabel(self)

        #Fig
        self.figure = QtWidgets.QLabel(self)
        self.figure.setEnabled(True)

        #Me
        self.lbl_Disclaimer = QtWidgets.QLabel("*This tool should only be used as an estimate and "
                                               "should not be considered 100% accurate || © Matt Caine - UoP - Comp3000 Project", self)

        #-----------------------------------------------------------------------------------------------Other section
        self.chbx_ids = QtWidgets.QCheckBox("Network IDS/IPS",self)
        self.chbx_ids.setToolTip('Simulates the presence of a Network IDS/IPS.')

        self.chbx_offline = QtWidgets.QCheckBox("Realistic Nodes", self)
        self.chbx_offline.setToolTip('Takes into account that devices may not be turned on 24/7.')

        self.chbx_offline.setChecked(True)

        self.chbx_HostFire = QtWidgets.QCheckBox("Host Based Firewalls", self)
        self.chbx_HostFire.setToolTip('Simulates the presence of host based firewalls.')

        #-------------------------------Dev----------------------------------------------

        self.chbx_4 = QtWidgets.QCheckBox("Awareness Training", self)
        #self.chbx_4.setToolTip('This is a tooltip for the QPushButton widget')

        self.chbx_5 = QtWidgets.QCheckBox("Coming Soon", self)
        #self.chbx_5.setToolTip('This is a tooltip for the QPushButton widget')
        self.chbx_6 = QtWidgets.QCheckBox("Coming Soon", self)
        # self.chbx_6.setToolTip('This is a tooltip for the QPushButton widget')
        self.chbx_7 = QtWidgets.QCheckBox("Coming Soon", self)
        # self.chbx_7.setToolTip('This is a tooltip for the QPushButton widget')
        self.chbx_8 = QtWidgets.QCheckBox("Coming Soon", self)
        # self.chbx_8.setToolTip('This is a tooltip for the QPushButton widget')

        # Disable buttons
        self.chbx_4.setEnabled(False)
        self.chbx_5.setEnabled(False)
        self.chbx_6.setEnabled(False)
        self.chbx_7.setEnabled(False)
        self.chbx_8.setEnabled(False)


        # Window frame settings
        self.setFixedSize(1700, 900)
        self.setWindowTitle("Computer Virus Spread Visualization Tool")
        self.initUI()
        self.simulate()

    def initUI(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setWindowOpacity(0.96)

        #window Icon
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #----------------------------------Form----------------------------------#
        self.header.setPixmap(self.Head_img)
        self.header.resize(1920, 50)

        self.WaterMark.setPixmap(self.WaterMark_img)
        self.WaterMark.resize(555, 482)
        self.WaterMark.move(580, 240)

        self.lbl_Disclaimer.setGeometry(1030, 875, 1000, 20)
        self.sbx_hibernation.setDisabled(True)
        self.sbx_mortality.setDisabled(True)

        # ----------------------------------Titles----------------------------------#


        self.lbl_simulation_Header.move(145, 50)
        self.lbl_Param_Header.move(15, 50)
        self.lbl_virus_Header.move(15, 260)
        self.lbl_other_Header.move(15, 470)
        self.lbl_actions_Header.move(15, 740)
        self.lbl_sim_name.move(220, 50)

        #----------------------------------parameter Section----------------------------------#

        #--------Virus Model--------#
        self.lbl_Virus_Model.move(20, 65)

        #✅❌
        self.cbx_Virus_Model.addItems(["S.I.R","S.I.R/D", "❌ S.E.I.R", "S.I.S","❌ S.E.I.S"])

        self.cbx_Virus_Model.setGeometry(19, 90, 100, 25)

        # Disable models
        self.cbx_Virus_Model.model().item(2).setEnabled(False)
        self.cbx_Virus_Model.model().item(4).setEnabled(False)

        self.cbx_Virus_Model.model().item(0).setToolTip('Susceptible ⇢ Infected ⇢ Recovered')
        self.cbx_Virus_Model.model().item(1).setToolTip('Susceptible ⇢ Infected ⇢ Recovered or Irrecoverable (Deceased)')
        self.cbx_Virus_Model.model().item(2).setToolTip('Susceptible ⇢ Exposed ⇢ Infected ⇢ Recovered')
        self.cbx_Virus_Model.model().item(3).setToolTip('Susceptible ⇢ Infected ⇢ Susceptible')
        self.cbx_Virus_Model.model().item(4).setToolTip('Susceptible ⇢ Exposed ⇢ Infected ⇢ Susceptible')


        self.cbx_Virus_Model.currentTextChanged.connect(self.on_model_combobox_changed)

        #--------Susceptible--------#
        self.lbl_healthy.setText("Overall Susceptible")
        self.lbl_healthy.move(20, 113)

        self.sbx_healthy.move(19, 137)
        self.sbx_healthy.setMinimum(1)
        self.sbx_healthy.setMaximum(1000000)
        self.sbx_healthy.setValue(25000)
        self.sbx_healthy.setSingleStep(100)

        self.sbx_healthy.setToolTip('1 to 1000000')


        #--------Infected--------#
        self.lbl_infected.setText("Starting Infected")
        self.lbl_infected.move(20, 161)

        self.sbx_infected.move(19, 185)
        self.sbx_infected.setMinimum(1)
        self.sbx_infected.setMaximum(1000000)
        self.sbx_infected.setValue(100)
        self.sbx_infected.setSingleStep(100)

        self.sbx_infected.setToolTip('1 to 1000000')

        #--------Iterations--------#
        self.lbl_days.setText("Hours | 168<")
        self.lbl_days.move(20, 209)

        self.sbx_days.move(19, 233)
        self.sbx_days.setMinimum(168)
        self.sbx_days.setMaximum(10001)
        self.sbx_days.setValue(336)
        self.sbx_days.setSingleStep(5)

        self.sbx_days.setToolTip('168 to 10000')

        # --------propagation--------#
        self.lbl_propagation.setText("Propagation Rate")
        self.lbl_propagation.resize(1000, 20)
        self.lbl_propagation.move(20, 279)
        self.sbx_propagation.move(19, 299)

        self.sbx_propagation.setMinimum(0)
        self.sbx_propagation.setMaximum(100)
        self.sbx_propagation.setValue(5)
        self.sbx_propagation.setSingleStep(5)

        self.sbx_propagation.setToolTip('1 to 100')

        # --------hibernation--------#
        self.lbl_hibernation.setText("Hibernation Time")
        self.lbl_hibernation.move(20, 323)
        self.sbx_hibernation.move(19, 347)

        self.sbx_hibernation.setMinimum(1)
        self.sbx_hibernation.setMaximum(10001)
        self.sbx_hibernation.setValue(0)
        self.sbx_hibernation.setSingleStep(10)

        self.sbx_hibernation.setToolTip('1 to 10000')

        # --------r_chance--------#
        self.lbl_r_chance.setText("Recovery Rate")
        self.lbl_r_chance.move(20, 371)
        self.sbx_r_chance.move(19, 395)

        self.sbx_r_chance.setMinimum(0)
        self.sbx_r_chance.setMaximum(100)
        self.sbx_r_chance.setValue(10)
        self.sbx_r_chance.setSingleStep(5)

        self.sbx_r_chance.setToolTip('1 to 100')

        # --------Mortality--------#
        self.lbl_mortality.setText("Irrecoverable Rate")
        self.lbl_mortality.move(20, 419)
        self.sbx_mortality.move(19, 443)

        self.sbx_mortality.setMinimum(0)
        self.sbx_mortality.setMaximum(100)
        self.sbx_mortality.setValue(5)
        self.sbx_mortality.setSingleStep(5)

        self.sbx_mortality.setToolTip('1 to 100')

        # ----------------------------------other Section----------------------------------#

        self.chbx_offline.move(19, 490)
        self.chbx_ids.move(19, 510)
        self.chbx_HostFire.move(19, 530)
        self.chbx_HostFire.resize(120, 30)

        self.chbx_4.move(19, 550)
        self.chbx_4.resize(120, 30)

        self.chbx_5.move(19, 570)
        self.chbx_6.move(19, 590)
        self.chbx_7.move(19, 610)
        self.chbx_8.move(19, 630)


        # ----------------------------------SIMSection----------------------------------#

        #--------Reset Button--------#
        self.btn_reset.move(19, 769)
        self.btn_reset.clicked.connect(self.reset_parameters)

        # --------undo Button--------#
        self.btn_undo.resize(30, 30)
        self.btn_undo.move(120, 769)
        self.btn_undo.setEnabled(False)

        self.btn_undo.setToolTip("Undo Reset | Coming Soon...")

        # --------info Button--------#
        self.btn_Info.resize(27, 27)
        self.btn_Info.move(120, 89)
        self.btn_Info.setToolTip("Find out more about the models")

        #--------Save Button--------#

        self.btn_Save.move(19, 805)
        self.btn_Save.clicked.connect(self.Save)

        # --------Open folder Button--------#
        self.btn_folder.resize(30, 30)
        self.btn_folder.move(120, 805)
        self.btn_folder.clicked.connect(self.open_save)

        self.btn_folder.setToolTip("Open Export Folder")

        #--------Run Sim Button--------#
        self.btn_simulate.move(19, 841)
        self.btn_simulate.clicked.connect(self.simulate)
        self.btn_simulate.clicked.connect(self.progressbar)

        # --------pin Button--------#

        self.btn_pin.resize(30,30)
        self.btn_pin.move(120, 841)
        self.btn_pin.setToolTip("Pins Current Figure into Separate Window")

        # Button Event
        self.sub_window = SubWindow()
        self.btn_pin.clicked.connect(self.set_pin)
        self.btn_pin.clicked.connect(self.sub_window.show)

    # ----------------------------------Functions----------------------------------#
    # --------Test Button--------#
    @staticmethod
    def Click_test():
        print("Button Clicked")

    def open_save(self):
        try:
            os.startfile("Saved")
        except Exception as e:
            self.msg_box.setText("🛑 Error | {} ".format(e))
            self.msg_box.exec_()

    def set_pin(self):
        try:
            self.sub_window.Fig_img = QPixmap('fig_temp.png')
            self.sub_window.figure.setPixmap(self.Fig_img)
            self.sub_window.figure.resize(self.Fig_img.width(), self.Fig_img.height())
        except Exception as e:
            self.msg_box.setText("🛑 Error | {} ".format(e))
            self.msg_box.exec_()

    # --------Progress--------#
    def progressbar(self):
        try:
            self.completed = 0
            self.progress.show()
            self.lbl_Disclaimer.hide()
            while self.completed < 100:
                self.completed += 0.0005
                self.progress.setValue(self.completed)
            self.progress.hide()
            self.lbl_Disclaimer.show()
        except Exception as e:
            self.msg_box.setText("🛑 {}".format(e))
            self.msg_box.exec_()

    # ----------ID----------#
    def make_ID(self):
        try:
            self.stamp = str(uuid.uuid4())[:5]
            self.model_stamp = self.cbx_Virus_Model.currentText()
            self.c1_model_stamp = self.model_stamp.replace('/', '')
            self.c2_model_stamp = self.c1_model_stamp.replace('.', '')
            self.ID_Stamp = str(self.c2_model_stamp + "-" + self.stamp)
        except Exception as e:
            self.msg_box.setText("🛑 {}".format(e))
            self.msg_box.exec_()

    # --------Save--------#
    def Save(self):
        try:
            self.figure.setEnabled(False)
            os.mkdir('Saved/{}'.format(self.ID_Stamp))
            self.img = QPixmap('fig_temp.png')
            self.img.save('Saved/{}/Figure.png'.format(self.ID_Stamp))

            with open('Saved/{}/Parameters.txt'.format(self.c2_model_stamp+"-"+self.stamp), 'w') as f:
                f.write('ID: {}\n'
                        'Model: {}\n\n'
                        'Overall Susceptible: {}\n'
                        'Starting Infected: {}\n'
                        'Hours Shown: {}\n\n'
                        'Propagation Rate: {}\n'
                        'Recovery Rate: {}\n'
                        'Mortality Rate: {}\n'
                        '# Mortality Only Applicable for S.I.R/D\n\n'.format(self.ID_Stamp,self.cbx_Virus_Model.currentText(),self.sbx_healthy.value(),
                                                                                    self.sbx_infected.value(),self.sbx_days.value(),self.sbx_propagation.value(),
                                                                                    self.sbx_r_chance.value(),self.sbx_mortality.value()))
            #show saved box
            self.Save_msg.setText("💾 | {} Saved! \n\n Figure & Parameters File created in '/Saved/{}'".format(self.ID_Stamp,self.ID_Stamp))
            self.Save_msg.exec_()
            self.figure.setEnabled(True)

        # Error msg box
        except Exception as e:
            self.msg_box.setText("🛑 Error | {} ".format(e))
            self.msg_box.exec_()
            self.figure.setEnabled(True)

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

    # --------Reset Button--------#
    def reset_parameters(self):
        self.figure.setEnabled(False)
        ret = QMessageBox.question(self, 'Parameter Reset', "🗑️ | Are you sure? This will reset all parameters.",
                                   QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            #self.cbx_Virus_Model.setCurrentIndex(0)
            self.sbx_healthy.setValue(25000)
            self.sbx_infected.setValue(100)
            self.sbx_days.setValue(336)
            self.sbx_propagation.setValue(5)
            self.sbx_hibernation.setValue(1)
            self.sbx_r_chance.setValue(10)
            self.cbx_viruses.setCurrentIndex(0)
            self.sbx_mortality.setValue(5)
            self.chbx_ids.setChecked(False)
            self.chbx_HostFire.setChecked(False)
            self.chbx_offline.setChecked(True)

            # Run Sim again to Clear
            self.simulate()
            self.figure.setEnabled(True)
        else:
            self.figure.setEnabled(True)

    def closeEvent(self, event):
        self.figure.setEnabled(False)
        close = QtWidgets.QMessageBox.question(self,"Close? ","❌ | Are you sure to Close?\n\nAny unsaved figures will be lost. ", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            self.figure.setEnabled(True)
            event.ignore()

    #--------------------------------------------------------------simulate MODELS------------------------------------------------------------------------#
    def simulate(self):
        try:
            # Make ID for this SIM
            self.make_ID()

            # Set ID in Lbl
            self.lbl_sim_name.setText(self.ID_Stamp)

            # Run Models
            # SIR
            if self.cbx_Virus_Model.currentIndex() == 0:
                SIR(self.sbx_healthy, self.sbx_infected, self.sbx_days,
                    self.sbx_propagation, self.sbx_r_chance, self.chbx_ids, self.chbx_offline,self.chbx_HostFire)

            # SIRD
            elif self.cbx_Virus_Model.currentIndex() == 1:
                SIRD(self.sbx_healthy, self.sbx_infected, self.sbx_days,
                     self.sbx_propagation, self.sbx_r_chance,self.sbx_mortality,self.chbx_ids, self.chbx_offline,self.chbx_HostFire)
            # SEIR
            elif self.cbx_Virus_Model.currentIndex() == 2:
                print()

            # SIS
            elif self.cbx_Virus_Model.currentIndex() == 3:
                SIS(self.sbx_healthy, self.sbx_infected, self.sbx_days,
                    self.sbx_propagation, self.sbx_r_chance,self.chbx_ids,self.chbx_offline,self.chbx_HostFire)

            # Show Results
            self.Fig_img = QPixmap('fig_temp.png')
            self.figure.setPixmap(self.Fig_img)
            self.figure.resize(self.Fig_img.width(), self.Fig_img.height())
            self.figure.move(148, 80)


        #Error Box
        except Exception as e:
            self.msg_box.setText("🛑 {}".format(e))
            self.msg_box.exec_()

class SubWindow(QMainWindow):
    def __init__(self):
        super(SubWindow, self).__init__()
        # Window--------------------------------------------------------#
        self.setWindowTitle("Computer Virus Spread Visualization Tool - 📌 Pinned Figure")
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.lbl_Disclaimer = QtWidgets.QLabel(self)
        self.lbl_Disclaimer.setText("*This tool should only be used as an estimate and should not be considered "
                                   "100% accurate | © Matt Caine - UoP - Comp3000 Project")
        self.lbl_Disclaimer.setGeometry(870, 785, 1000, 20)

        # Grab and set Image --------------------------------------------------#
        self.figure = QtWidgets.QLabel(self)
        self.setFixedSize(1530, 810)

        # Opacity Slider --------------------------------------------------#
        slider = QtWidgets.QSlider(self)
        slider.setGeometry(15, 690, 25, 100)
        slider.setRange(65,100)
        slider.setValue(355)

        self.lbl_WindowOpacity = QtWidgets.QLabel(self)
        self.lbl_WindowOpacity.setText("𝗢𝗣𝗔𝗖𝗜𝗧𝗬: " + str(slider.value()/100))
        self.lbl_WindowOpacity.move(5,785)
        slider.valueChanged.connect(lambda: do_action())
        def do_action():
            # setting text to the label
            self.lbl_WindowOpacity.setText("𝗢𝗣𝗔𝗖𝗜𝗧𝗬: " + str(slider.value()/100))
            self.setWindowOpacity(slider.value()/100)

        # END----------------------------------------------------------#

# --------------Window Order--------------#
def window():
    print("[Start]")
    app = QApplication(sys.argv)
    win = Window()
    splash = Splash()
    splash.show()
    time.sleep(1)
    Disclaimer()
    splash.hide()
    print("[Execute Main Window]")
    win.show()
    sys.exit(app.exec_())
try:
    window()
except Exception as e:
    print(e)

