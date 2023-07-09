# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == QtCore.Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 3)
        self.comboBox_BinFileCoding = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_BinFileCoding.setFont(font)
        self.comboBox_BinFileCoding.setObjectName("comboBox_BinFileCoding")
        self.comboBox_BinFileCoding.addItem("")
        self.comboBox_BinFileCoding.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_BinFileCoding, 4, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_PointsCountOnChannel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PointsCountOnChannel.setFont(font)
        self.label_PointsCountOnChannel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PointsCountOnChannel.setObjectName("label_PointsCountOnChannel")
        self.gridLayout_2.addWidget(self.label_PointsCountOnChannel, 5, 0, 1, 3)

        self.label_PointsCountOnChannelVal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PointsCountOnChannelVal.setFont(font)
        self.label_PointsCountOnChannelVal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PointsCountOnChannelVal.setObjectName("label_PointsCountOnChannelVal")
        self.gridLayout_2.addWidget(self.label_PointsCountOnChannelVal, 5, 3, 1, 1)

        self.spinBox_DataSampleFreq = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_DataSampleFreq.setFont(font)
        self.spinBox_DataSampleFreq.setObjectName("spinBox_DataSampleFreq")
        self.gridLayout_2.addWidget(self.spinBox_DataSampleFreq, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 3)
        self.SpinBox_SignalDuration = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpinBox_SignalDuration.setFont(font)
        self.SpinBox_SignalDuration.setObjectName("SpinBox_SignalDuration")
        self.gridLayout_2.addWidget(self.SpinBox_SignalDuration, 3, 3, 1, 1)
        self.label_channels_count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_channels_count.setFont(font)
        self.label_channels_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channels_count.setObjectName("label_channels_count")
        self.gridLayout_2.addWidget(self.label_channels_count, 0, 0, 1, 3)

        self.label_used_channels = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_used_channels.setFont(font)
        self.label_used_channels.setAlignment(QtCore.Qt.AlignCenter)
        self.label_used_channels.setObjectName("label_used_channels")
        self.gridLayout_2.addWidget(self.label_used_channels, 1, 0, 1, 3)

        self.spinBox_ChannelsCount = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_ChannelsCount.setFont(font)
        self.spinBox_ChannelsCount.setObjectName("spinBox_ChannelsCount")
        self.gridLayout_2.addWidget(self.spinBox_ChannelsCount, 0, 3, 1, 1)

        self.comboBox_UsedChannels = CheckableComboBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_UsedChannels.setFont(font)
        self.comboBox_UsedChannels.setObjectName("comboBox_UsedChannels")
        self.gridLayout_2.addWidget(self.comboBox_UsedChannels, 1, 3, 1, 1)

        self.pushButton_RunHandling = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_RunHandling.setFont(font)
        self.pushButton_RunHandling.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_RunHandling.setObjectName("pushButton_RunHandling")
        self.gridLayout_2.addWidget(self.pushButton_RunHandling, 8, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 3)
        # spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        # self.label_12 = QtWidgets.QLabel(self.centralwidget)
        # self.label_12.setText("")
        # self.label_12.setObjectName("label_12")
        # self.gridLayout_2.addWidget(self.label_12, 14, 0, 1, 1)
        # self.label_13 = QtWidgets.QLabel(self.centralwidget)
        # self.label_13.setText("")
        # self.label_13.setObjectName("label_13")
        # self.gridLayout_2.addWidget(self.label_13, 15, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Кодировка вещественных чисел"))
        self.comboBox_BinFileCoding.setItemText(0, _translate("MainWindow", "double (8 байт)"))
        #self.comboBox_BinFileCoding.setItemText(1, _translate("MainWindow", "float (4 байта)"))
        self.label_PointsCountOnChannel.setText(_translate("MainWindow", "Количество точек на 1 канал"))
        self.label_2.setText(_translate("MainWindow", "Частота сбора данных, Гц"))
        self.pushButton_RunHandling.setText(_translate("MainWindow", "Далее"))
        self.label_3.setText(_translate("MainWindow", "Длительность сигнала на 1 канале, сек"))
        self.label_used_channels.setText(_translate("MainWindow", "Используемые каналы"))
        self.label_channels_count.setText(_translate("MainWindow", "Кол-во каналов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
