# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from superqt import QLabeledRangeSlider


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_DataSize = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DataSize.setFont(font)
        self.label_DataSize.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DataSize.setObjectName("label_DataSize")
        self.gridLayout_2.addWidget(self.label_DataSize, 0, 0, 1, 3)

        self.label_DataSizeVal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DataSizeVal.setFont(font)
        self.label_DataSizeVal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DataSizeVal.setObjectName("label_DataSizeVal")
        self.gridLayout_2.addWidget(self.label_DataSizeVal, 0, 3, 1, 1)

        self.label_MeasureTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_MeasureTime.setFont(font)
        self.label_MeasureTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MeasureTime.setObjectName("label_MeasureTime")
        self.gridLayout_2.addWidget(self.label_MeasureTime, 1, 0, 1, 3)

        self.label_MeasureTimeVal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_MeasureTimeVal.setFont(font)
        self.label_MeasureTimeVal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MeasureTimeVal.setObjectName("label_MeasureTimeVal")
        self.gridLayout_2.addWidget(self.label_MeasureTimeVal, 1, 3, 1, 1)

        self.label_ThrownPoints = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ThrownPoints.setFont(font)
        self.label_ThrownPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ThrownPoints.setObjectName("label_ThrownPoints")
        self.gridLayout_2.addWidget(self.label_ThrownPoints, 2, 0, 1, 3)

        self.spinBox_ThrownPoints = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_ThrownPoints.setFont(font)
        self.spinBox_ThrownPoints.setObjectName("spinBox_ThrownPoints")
        self.gridLayout_2.addWidget(self.spinBox_ThrownPoints, 2, 3, 1, 1)

        self.label_WhatToDo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setPointSize(12)
        self.label_WhatToDo.setFont(font)
        self.label_WhatToDo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WhatToDo.setObjectName("label_WhatToDo")
        self.gridLayout_2.addWidget(self.label_WhatToDo, 3, 0, 1, 4)

        self.label_Start = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Start.setFont(font)
        self.label_Start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Start.setObjectName("label_Start")
        self.gridLayout_2.addWidget(self.label_Start, 4, 0, 1, 3)

        self.label_End = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_End.setFont(font)
        self.label_End.setAlignment(QtCore.Qt.AlignCenter)
        self.label_End.setObjectName("label_End")
        self.gridLayout_2.addWidget(self.label_End, 5, 0, 1, 3)

        self.spinBox_AnalyzingTStart = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_AnalyzingTStart.setFont(font)
        self.spinBox_AnalyzingTStart.setObjectName("spinBox_AnalyzingTStart")
        self.gridLayout_2.addWidget(self.spinBox_AnalyzingTStart, 4, 3, 1, 1)

        self.spinBox_AnalyzingTEnd = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_AnalyzingTEnd.setFont(font)
        self.spinBox_AnalyzingTEnd.setObjectName("spinBox_AnalyzingTEnd")
        self.gridLayout_2.addWidget(self.spinBox_AnalyzingTEnd, 5, 3, 1, 1)

        # self.sliderAnalyzingTime = QLabeledRangeSlider()
        # self.sliderAnalyzingTime.setOrientation(1)
        # self.sliderAnalyzingTime.setObjectName("sliderAnalyzingTime")
        # self.gridLayout_2.addWidget(self.sliderAnalyzingTime, 4, 0, 1, 4)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.gridLayout_2.addWidget(self.label_status, 7, 0, 1, 4)

        self.pushButton_RunHandling = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_RunHandling.setFont(font)
        self.pushButton_RunHandling.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_RunHandling.setObjectName("pushButton_RunHandling")
        self.gridLayout_2.addWidget(self.pushButton_RunHandling, 8, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_MeasureTime.setText(_translate("MainWindow", "Время сбора данных, сек"))
        self.label_ThrownPoints.setText(_translate("MainWindow", "Кол-во выбрасываемых точек"))
        self.label_DataSize.setText(_translate("MainWindow", "Зарегистрированных данных АЦП"))
        self.label_WhatToDo.setText(_translate("MainWindow", "Aнализируемый временной промежуток:"))
        self.label_status.setText(_translate("MainWindow", " "))
        self.label_11.setText(_translate("MainWindow", " "))
        self.label_Start.setText(_translate("MainWindow", "Начало, сек"))
        self.label_End.setText(_translate("MainWindow", "Конец, сек"))
        self.pushButton_RunHandling.setText(_translate("MainWindow", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
