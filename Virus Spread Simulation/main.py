import sys
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # ----------------------------------Declare----------------------------------#

        #Run Button
        self.btn_simulate = QtWidgets.QPushButton(self)
        #Param Reset button
        self.btn_reset = QtWidgets.QPushButton(self)
        # Iterations group
        self.sbx_iterations = QtWidgets.QSpinBox(self)
        self.lbl_iterations = QtWidgets.QLabel(self)
        # Infected group
        self.sbx_infected = QtWidgets.QSpinBox(self)
        self.lbl_infected = QtWidgets.QLabel(self)
        # Healthy group
        self.sbx_healthy = QtWidgets.QSpinBox(self)
        self.lbl_healthy = QtWidgets.QLabel(self)
        # Header Img
        self.Head_img = QPixmap('assets/img/Header.png')
        self.header = QtWidgets.QLabel(self)
        # Networks group
        self.lbl_networks = QtWidgets.QLabel(self)
        self.sbx_networks = QtWidgets.QSpinBox(self)

        # Window frame settings
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Comp3000 - Computer Virus Spread Simulation")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('assets/img/Header.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        #end
        self.initUI()

    def initUI(self):

        # Design Notes to remember
        # 25p gap between object and label
        # 30p Gap between each pair

        #----------------------------------Header----------------------------------#

        self.header.setPixmap(self.Head_img)
        self.header.resize(1000, 50)

        #----------------------------------parameter Section----------------------------------#

        #--------Networks--------#
        self.lbl_networks.setText("Networks")
        self.lbl_networks.move(20, 65)

        self.sbx_networks.move(19, 90)
        self.sbx_networks.setMinimum(1)
        self.sbx_networks.setMaximum(99999)
        self.sbx_networks.setValue(100)
        self.sbx_networks.setSingleStep(100)

        #--------Healthy--------#
        self.lbl_healthy.setText("Healthy")
        self.lbl_healthy.move(20, 120)

        self.sbx_healthy.move(19, 145)
        self.sbx_healthy.setMinimum(1)
        self.sbx_healthy.setMaximum(99999)
        self.sbx_healthy.setValue(25000)
        self.sbx_healthy.setSingleStep(100)

        #--------Infected--------#
        self.lbl_infected.setText("Infected")
        self.lbl_infected.move(20, 175)

        self.sbx_infected.move(19, 200)
        self.sbx_infected.setMinimum(1)
        self.sbx_infected.setMaximum(99999)
        self.sbx_infected.setValue(100)
        self.sbx_infected.setSingleStep(100)

        #--------Iterations--------#
        self.lbl_iterations.setText("Days")
        self.lbl_iterations.move(20, 230)

        self.sbx_iterations.move(19, 255)
        self.sbx_iterations.setMinimum(10)
        self.sbx_iterations.setMaximum(365)
        self.sbx_iterations.setValue(100)
        self.sbx_iterations.setSingleStep(5)

        #--------Reset Button--------#
        self.btn_reset.setText("Reset")
        self.btn_reset.move(19, 300)
        self.btn_reset.clicked.connect(self.reset_parameters)


        # ----------------------------------Simulate----------------------------------#
        self.btn_simulate.setText("Simulate")
        self.btn_simulate.move(19, 650)
        self.btn_simulate.clicked.connect(self.Click_test)

    # ----------------------------------Functions----------------------------------#
    # --------Test Button--------#
    @staticmethod
    def Click_test():
        print("Button Clicked")

    # --------Parameter Reset Button--------#
    def reset_parameters(self):
        ret = QMessageBox.question(self, 'Parameter Reset', "Are you sure you want to reset the parameters?",
                                   QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.sbx_networks.setValue(100)
            self.sbx_healthy.setValue(25000)
            self.sbx_infected.setValue(100)
            self.sbx_iterations.setValue(100)


# ----------------------------------Window----------------------------------#
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

