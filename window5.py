# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window5.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle

class Ui_window5(object):
    def setupUi(self, window5):
        window5.setObjectName("window5")
        window5.resize(920, 475)
        window5.setStyleSheet(lightstyle.css)
        window5.setWindowIcon(QtGui.QIcon('icons/favicon.ico'))
        self.centralwidget = QtWidgets.QWidget(window5)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.semester_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.semester_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.gridLayout.addWidget(self.semester_combobox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.inputType_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.inputType_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputType_combobox.setFont(font)
        self.inputType_combobox.setObjectName("inputType_combobox")
        self.gridLayout.addWidget(self.inputType_combobox, 2, 0, 1, 1)
        self.generated_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generated_table.sizePolicy().hasHeightForWidth())
        self.generated_table.setSizePolicy(sizePolicy)
        self.generated_table.setMinimumSize(QtCore.QSize(596, 290))
        self.generated_table.setObjectName("generated_table")
        self.generated_table.setColumnCount(8)
        self.generated_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.generated_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_table.setHorizontalHeaderItem(7, item)
        self.generated_table.horizontalHeader().setDefaultSectionSize(100)
        self.generated_table.horizontalHeader().setMinimumSectionSize(37)
        self.generated_table.verticalHeader().setDefaultSectionSize(43)
        self.generated_table.verticalHeader().setMinimumSectionSize(27)
        self.gridLayout.addWidget(self.generated_table, 3, 0, 1, 4)
        self.faculty_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.faculty_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.faculty_combobox.setFont(font)
        self.faculty_combobox.setObjectName("faculty_combobox")
        self.gridLayout.addWidget(self.faculty_combobox, 2, 3, 1, 1)
        self.section_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.section_combobox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.section_combobox.setFont(font)
        self.section_combobox.setObjectName("section_combobox")
        self.gridLayout.addWidget(self.section_combobox, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.roomno_textbox = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomno_textbox.sizePolicy().hasHeightForWidth())
        self.roomno_textbox.setSizePolicy(sizePolicy)
        self.roomno_textbox.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.roomno_textbox.setFont(font)
        self.roomno_textbox.setObjectName("roomno_textbox")
        self.horizontalLayout.addWidget(self.roomno_textbox)
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.finishBtn = QtWidgets.QPushButton(self.centralwidget)
        self.finishBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.finishBtn.setFont(font)
        self.finishBtn.setObjectName("finishBtn")
        self.horizontalLayout.addWidget(self.finishBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        window5.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(window5)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionLoad = QtWidgets.QAction(window5)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut("Ctrl+L")
        self.actionExit = QtWidgets.QAction(window5)
        self.actionExit.setObjectName("actionExit")
        #self.actionExit.triggered.connect(self.closeEvent)
        self.actionAbout = QtWidgets.QAction(window5)
        self.actionAbout.setObjectName("actionAbout")
        self.actionManual = QtWidgets.QAction(window5)
        self.actionManual.setObjectName("actionManual")
        self.actionClear_All = QtWidgets.QAction(window5)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionClear_All.setShortcut("Ctrl+R")
        self.actionSet_Year_Department = QtWidgets.QAction(window5)
        self.actionSet_Year_Department.setObjectName("actionSet_Year_Department")
        self.aboutMenu = QtWidgets.QAction(window5)
        self.aboutMenu.setObjectName("aboutMenu")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_Year_Department)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.aboutMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(window5)
        QtCore.QMetaObject.connectSlotsByName(window5)
        window5.setTabOrder(self.inputType_combobox, self.semester_combobox)
        window5.setTabOrder(self.semester_combobox, self.section_combobox)
        window5.setTabOrder(self.section_combobox, self.faculty_combobox)
        window5.setTabOrder(self.faculty_combobox, self.generated_table)
        window5.setTabOrder(self.generated_table, self.roomno_textbox)
        window5.setTabOrder(self.roomno_textbox, self.printBtn)
        window5.setTabOrder(self.printBtn, self.backBtn)
        window5.setTabOrder(self.backBtn, self.finishBtn)

    def retranslateUi(self, window5):
        _translate = QtCore.QCoreApplication.translate
        window5.setWindowTitle(_translate("window5", "TimeTable Generator"))
        self.label_4.setText(_translate("window5", "Section:"))
        self.label_5.setText(_translate("window5", "Faculty:"))
        item = self.generated_table.verticalHeaderItem(0)
        item.setText(_translate("window5", "Monday"))
        item = self.generated_table.verticalHeaderItem(1)
        item.setText(_translate("window5", "Tuesday"))
        item = self.generated_table.verticalHeaderItem(2)
        item.setText(_translate("window5", "Wednesday"))
        item = self.generated_table.verticalHeaderItem(3)
        item.setText(_translate("window5", "Thursday"))
        item = self.generated_table.verticalHeaderItem(4)
        item.setText(_translate("window5", "Friday"))
        item = self.generated_table.verticalHeaderItem(5)
        item.setText(_translate("window5", "Saturday"))
        item = self.generated_table.horizontalHeaderItem(0)
        item.setText(_translate("window5", "9:00-9:55"))
        item = self.generated_table.horizontalHeaderItem(1)
        item.setText(_translate("window5", "9:55-10:50"))
        item = self.generated_table.horizontalHeaderItem(2)
        item.setText(_translate("window5", "11:10-12:05"))
        item = self.generated_table.horizontalHeaderItem(3)
        item.setText(_translate("window5", "12:05-1:00"))
        item = self.generated_table.horizontalHeaderItem(4)
        item.setText(_translate("window5", "1:00-1:55"))
        item = self.generated_table.horizontalHeaderItem(5)
        item.setText(_translate("window5", "1:55-2:50"))
        item = self.generated_table.horizontalHeaderItem(6)
        item.setText(_translate("window5", "2:50-3:40"))
        item = self.generated_table.horizontalHeaderItem(7)
        item.setText(_translate("window5", "3:40-4:30"))
        self.label_3.setText(_translate("window5", "Semester:"))
        self.label_6.setText(_translate("window5", "Room Number:"))
        self.printBtn.setText(_translate("window5", "Print"))
        self.backBtn.setText(_translate("window5", "Back"))
        self.finishBtn.setText(_translate("window5", "Finish"))
        self.label_2.setText(_translate("window5", "Input Type:"))
        self.label.setText(_translate("window5", "Generated Timetable"))
        self.menuFile.setTitle(_translate("window5", "File"))
        self.menuHelp.setTitle(_translate("window5", "Help"))
        self.actionSave.setText(_translate("window5", "Save"))
        self.actionLoad.setText(_translate("window5", "Load"))
        self.actionExit.setText(_translate("window5", "Exit"))
        self.actionAbout.setText(_translate("window5", "About"))
        self.actionManual.setText(_translate("window5", "Manual"))
        self.actionSet_Year_Department.setText(_translate("window5", "Set Year/Department"))
        self.actionClear_All.setText(_translate("window5", "Clear All"))
        self.aboutMenu.setText(_translate("window5", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window5 = QtWidgets.QMainWindow()
    ui = Ui_window5()
    ui.setupUi(window5)
    window5.show()
    sys.exit(app.exec_())

