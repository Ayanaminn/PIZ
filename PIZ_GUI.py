# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIZ_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.light_A = QtWidgets.QLabel(self.centralwidget)
        self.light_A.setGeometry(QtCore.QRect(30, 420, 81, 31))
        self.light_A.setFrameShape(QtWidgets.QFrame.Box)
        self.light_A.setObjectName("light_A")
        self.light_B = QtWidgets.QLabel(self.centralwidget)
        self.light_B.setGeometry(QtCore.QRect(120, 420, 71, 31))
        self.light_B.setFrameShape(QtWidgets.QFrame.Box)
        self.light_B.setObjectName("light_B")
        self.light_loop = QtWidgets.QLabel(self.centralwidget)
        self.light_loop.setGeometry(QtCore.QRect(30, 470, 161, 21))
        self.light_loop.setFrameShape(QtWidgets.QFrame.Box)
        self.light_loop.setObjectName("light_loop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 500, 71, 16))
        self.label.setObjectName("label")
        self.loop_counter_label = QtWidgets.QLabel(self.centralwidget)
        self.loop_counter_label.setGeometry(QtCore.QRect(110, 500, 47, 16))
        self.loop_counter_label.setObjectName("loop_counter_label")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(310, 20, 781, 151))
        self.treeWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget.setColumnCount(0)
        self.treeWidget.setObjectName("treeWidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setEnabled(False)
        self.start_button.setGeometry(QtCore.QRect(770, 440, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 180, 1081, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(60, -10, 61, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 1081, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(720, 0, 61, 121))
        self.frame_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(390, 0, 61, 151))
        self.frame_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.state_a = QtWidgets.QComboBox(self.frame)
        self.state_a.setGeometry(QtCore.QRect(190, 50, 69, 22))
        self.state_a.setEditable(True)
        self.state_a.setCurrentText("")
        self.state_a.setObjectName("state_a")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(550, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.state_b = QtWidgets.QComboBox(self.frame)
        self.state_b.setGeometry(QtCore.QRect(520, 50, 69, 22))
        self.state_b.setEditable(True)
        self.state_b.setCurrentText("")
        self.state_b.setObjectName("state_b")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(610, 50, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(440, 50, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 50, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 1081, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.time_a = QtWidgets.QSpinBox(self.frame)
        self.time_a.setGeometry(QtCore.QRect(341, 50, 71, 22))
        self.time_a.setMinimum(1)
        self.time_a.setMaximum(86400)
        self.time_a.setObjectName("time_a")
        self.time_b = QtWidgets.QSpinBox(self.frame)
        self.time_b.setGeometry(QtCore.QRect(670, 50, 71, 22))
        self.time_b.setMinimum(1)
        self.time_b.setMaximum(86400)
        self.time_b.setObjectName("time_b")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(880, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(770, 50, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.state_c = QtWidgets.QComboBox(self.frame)
        self.state_c.setGeometry(QtCore.QRect(840, 50, 69, 22))
        self.state_c.setEditable(True)
        self.state_c.setCurrentText("")
        self.state_c.setObjectName("state_c")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(940, 50, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.time_c = QtWidgets.QSpinBox(self.frame)
        self.time_c.setGeometry(QtCore.QRect(1000, 50, 71, 22))
        self.time_c.setMinimum(1)
        self.time_c.setMaximum(86400)
        self.time_c.setObjectName("time_c")
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_7.raise_()
        self.frame_5.raise_()
        self.state_a.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.state_b.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.frame_2.raise_()
        self.time_a.raise_()
        self.time_b.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.state_c.raise_()
        self.label_11.raise_()
        self.time_c.raise_()
        self.add_rule_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_rule_button.setGeometry(QtCore.QRect(690, 270, 71, 31))
        self.add_rule_button.setObjectName("add_rule_button")
        self.reset_rule_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_rule_button.setGeometry(QtCore.QRect(590, 270, 71, 31))
        self.reset_rule_button.setObjectName("reset_rule_button")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(780, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.total_cycle = QtWidgets.QSpinBox(self.centralwidget)
        self.total_cycle.setGeometry(QtCore.QRect(870, 280, 61, 22))
        self.total_cycle.setMinimum(1)
        self.total_cycle.setObjectName("total_cycle")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 281, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.port_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.port_comboBox.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.port_comboBox.setEditable(True)
        self.port_comboBox.setObjectName("port_comboBox")
        self.port_connect_button = QtWidgets.QPushButton(self.groupBox)
        self.port_connect_button.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.port_connect_button.setObjectName("port_connect_button")
        self.port_disconnect_button = QtWidgets.QPushButton(self.groupBox)
        self.port_disconnect_button.setEnabled(False)
        self.port_disconnect_button.setGeometry(QtCore.QRect(100, 90, 81, 31))
        self.port_disconnect_button.setObjectName("port_disconnect_button")
        self.port_refresh_button = QtWidgets.QPushButton(self.groupBox)
        self.port_refresh_button.setGeometry(QtCore.QRect(180, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.port_refresh_button.setFont(font)
        self.port_refresh_button.setObjectName("port_refresh_button")
        self.apply_setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_setting_button.setGeometry(QtCore.QRect(950, 270, 131, 31))
        self.apply_setting_button.setObjectName("apply_setting_button")
        self.light_C = QtWidgets.QLabel(self.centralwidget)
        self.light_C.setGeometry(QtCore.QRect(200, 420, 71, 31))
        self.light_C.setFrameShape(QtWidgets.QFrame.Box)
        self.light_C.setObjectName("light_C")
        self.frame.raise_()
        self.light_A.raise_()
        self.light_B.raise_()
        self.light_loop.raise_()
        self.label.raise_()
        self.loop_counter_label.raise_()
        self.treeWidget.raise_()
        self.start_button.raise_()
        self.add_rule_button.raise_()
        self.reset_rule_button.raise_()
        self.label_13.raise_()
        self.total_cycle.raise_()
        self.groupBox.raise_()
        self.apply_setting_button.raise_()
        self.light_C.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.light_A.setText(_translate("MainWindow", "A"))
        self.light_B.setText(_translate("MainWindow", "B"))
        self.light_loop.setText(_translate("MainWindow", " Loop"))
        self.label.setText(_translate("MainWindow", "Loop counter"))
        self.loop_counter_label.setText(_translate("MainWindow", "0"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.label_2.setText(_translate("MainWindow", "Condition"))
        self.label_3.setText(_translate("MainWindow", "Time(s)"))
        self.label_4.setText(_translate("MainWindow", "Channel A"))
        self.label_5.setText(_translate("MainWindow", "Channel B"))
        self.label_6.setText(_translate("MainWindow", "Time(s)"))
        self.label_7.setText(_translate("MainWindow", "Condition"))
        self.label_8.setText(_translate("MainWindow", "Step"))
        self.label_9.setText(_translate("MainWindow", "Channel C"))
        self.label_10.setText(_translate("MainWindow", "Condition"))
        self.label_11.setText(_translate("MainWindow", "Time(s)"))
        self.add_rule_button.setText(_translate("MainWindow", "ADD"))
        self.reset_rule_button.setText(_translate("MainWindow", "RESET"))
        self.label_13.setText(_translate("MainWindow", "Trial Cycle"))
        self.groupBox.setTitle(_translate("MainWindow", "Select device"))
        self.port_connect_button.setText(_translate("MainWindow", "Connect"))
        self.port_disconnect_button.setText(_translate("MainWindow", "Disconnect"))
        self.port_refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.apply_setting_button.setText(_translate("MainWindow", "APPLY"))
        self.light_C.setText(_translate("MainWindow", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
