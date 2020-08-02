# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTabWidget,QVBoxLayout,QWidget,\
                            QGridLayout,QGroupBox,QTextEdit,QLabel,QFrame,QSpacerItem,QSizePolicy,\
                            QHBoxLayout,QCommandLinkButton
from matplotlib.pyplot import figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,\
                                               NavigationToolbar2QT as NavigationToolbar


def clear(self):
    self.figure2.clear()
    self.figure1.clear()
    self.figure.clear()
class Ui_MainWindow(object):
    def plot(self, data):
        ax = self.figure.add_subplot(111)
        ax.plot(data[3], data[0])
        ax.set_ylabel("θ, гр.")
        ax.set_xlabel("t, с")
        ax.set_title("График зависимости угла наклона вектора скорости от времени\n")
        self.canvas.draw()


        ax = self.figure1.add_subplot(111)
        ax.plot(data[3], data[2])
        ax.set_ylabel("ϑ, гр.")
        ax.set_xlabel("t, с")
        ax.set_title("График зависимости угла тангажа от времени\n")
        self.canvas1.draw()


        ax = self.figure2.add_subplot(111)
        ax.plot(data[4], data[1])
        ax.set_ylabel("H, м")
        ax.set_xlabel("L, км")
        ax.set_title("График зависимости высоты от линейной дальности\n")
        self.canvas2.draw()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 800)
        MainWindow.setMinimumSize(QtCore.QSize(991, 686))
        self.MainLayout = QVBoxLayout(MainWindow)
        self.MainLayout.setObjectName("MainLayout")
        self.tabWidget = QTabWidget()
        self.MainLayout.addWidget(self.tabWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.textEdit_8 = QTextEdit(self.groupBox_3)
        self.textEdit_8.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout_9.addWidget(self.textEdit_8, 0, 1, 1, 1)
        self.textEdit_9 = QTextEdit(self.groupBox_3)
        self.textEdit_9.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout_9.addWidget(self.textEdit_9, 2, 1, 1, 1)
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 3, 0, 1, 1)
        self.textEdit_10 = QTextEdit(self.groupBox_3)
        self.textEdit_10.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout_9.addWidget(self.textEdit_10, 3, 1, 1, 1)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)
        self.textEdit_25 = QTextEdit(self.groupBox_3)
        self.textEdit_25.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_25.setObjectName("textEdit_25")
        self.gridLayout_9.addWidget(self.textEdit_25, 4, 1, 1, 1)
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_9.addWidget(self.label_25, 4, 0, 1, 1)
        self.label_88 = QLabel(self.groupBox_3)
        self.label_88.setObjectName("label_88")
        self.gridLayout_9.addWidget(self.label_88, 0, 2, 1, 1)
        self.label_89 = QLabel(self.groupBox_3)
        self.label_89.setObjectName("label_89")
        self.gridLayout_9.addWidget(self.label_89, 2, 2, 1, 1)
        self.label_90 = QLabel(self.groupBox_3)
        self.label_90.setObjectName("label_90")
        self.gridLayout_9.addWidget(self.label_90, 3, 2, 1, 1)
        self.label_91 = QLabel(self.groupBox_3)
        self.label_91.setObjectName("label_91")
        self.gridLayout_9.addWidget(self.label_91, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 7, 1, 2, 1)
        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.textEdit_55 = QTextEdit(self.groupBox_9)
        self.textEdit_55.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_55.setObjectName("textEdit_55")
        self.gridLayout_10.addWidget(self.textEdit_55, 1, 1, 1, 1)
        self.textEdit_54 = QTextEdit(self.groupBox_9)
        self.textEdit_54.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_54.setObjectName("textEdit_54")
        self.gridLayout_10.addWidget(self.textEdit_54, 0, 1, 1, 1)
        self.label_55 = QLabel(self.groupBox_9)
        self.label_55.setObjectName("label_55")
        self.gridLayout_10.addWidget(self.label_55, 1, 0, 1, 1)
        self.label_54 = QLabel(self.groupBox_9)
        self.label_54.setObjectName("label_54")
        self.gridLayout_10.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_92 = QLabel(self.groupBox_9)
        self.label_92.setObjectName("label_92")
        self.gridLayout_10.addWidget(self.label_92, 1, 2, 1, 1)
        self.label_93 = QLabel(self.groupBox_9)
        self.label_93.setObjectName("label_93")
        self.gridLayout_10.addWidget(self.label_93, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_9, 7, 2, 1, 1)
        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName("label_44")
        self.gridLayout_4.addWidget(self.label_44, 0, 0, 1, 1)
        self.textEdit_44 = QTextEdit(self.groupBox_6)
        self.textEdit_44.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_44.setObjectName("textEdit_44")
        self.gridLayout_4.addWidget(self.textEdit_44, 0, 1, 1, 1)
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName("label_45")
        self.gridLayout_4.addWidget(self.label_45, 2, 0, 1, 1)
        self.textEdit_45 = QTextEdit(self.groupBox_6)
        self.textEdit_45.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_45.setObjectName("textEdit_45")
        self.gridLayout_4.addWidget(self.textEdit_45, 2, 1, 1, 1)
        self.label_46 = QLabel(self.groupBox_6)
        self.label_46.setObjectName("label_46")
        self.gridLayout_4.addWidget(self.label_46, 3, 0, 1, 1)
        self.textEdit_47 = QTextEdit(self.groupBox_6)
        self.textEdit_47.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_47.setObjectName("textEdit_47")
        self.gridLayout_4.addWidget(self.textEdit_47, 4, 1, 1, 1)
        self.label_47 = QLabel(self.groupBox_6)
        self.label_47.setObjectName("label_47")
        self.gridLayout_4.addWidget(self.label_47, 4, 0, 1, 1)
        self.textEdit_46 = QTextEdit(self.groupBox_6)
        self.textEdit_46.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_46.setObjectName("textEdit_46")
        self.gridLayout_4.addWidget(self.textEdit_46, 3, 1, 1, 1)
        self.label_69 = QLabel(self.groupBox_6)
        self.label_69.setObjectName("label_69")
        self.gridLayout_4.addWidget(self.label_69, 0, 2, 1, 1)
        self.label_70 = QLabel(self.groupBox_6)
        self.label_70.setObjectName("label_70")
        self.gridLayout_4.addWidget(self.label_70, 2, 2, 1, 1)
        self.label_71 = QLabel(self.groupBox_6)
        self.label_71.setObjectName("label_71")
        self.gridLayout_4.addWidget(self.label_71, 3, 2, 1, 1)
        self.label_72 = QLabel(self.groupBox_6)
        self.label_72.setObjectName("label_72")
        self.gridLayout_4.addWidget(self.label_72, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 1, 4, 1, 1)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.textEdit_2 = QTextEdit(self.groupBox)
        self.textEdit_2.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 2, 1, 1, 1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.textEdit_4 = QTextEdit(self.groupBox)
        self.textEdit_4.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 5, 1, 1, 1)
        self.label_61 = QLabel(self.groupBox)
        self.label_61.setObjectName("label_61")
        self.gridLayout_2.addWidget(self.label_61, 0, 2, 1, 1)
        self.textEdit_3 = QTextEdit(self.groupBox)
        self.textEdit_3.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 4, 1, 1, 1)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_62 = QLabel(self.groupBox)
        self.label_62.setObjectName("label_62")
        self.gridLayout_2.addWidget(self.label_62, 4, 2, 1, 1)
        self.label_63 = QLabel(self.groupBox)
        self.label_63.setObjectName("label_63")
        self.gridLayout_2.addWidget(self.label_63, 5, 2, 1, 1)
        self.label_64 = QLabel(self.groupBox)
        self.label_64.setObjectName("label_64")
        self.gridLayout_2.addWidget(self.label_64, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_82 = QLabel(self.groupBox_4)
        self.label_82.setFrameShape(QFrame.NoFrame)
        self.label_82.setFrameShadow(QFrame.Plain)
        self.label_82.setLineWidth(1)
        self.label_82.setMidLineWidth(0)
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.gridLayout_8.addWidget(self.label_82, 1, 2, 1, 1)
        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName("label_26")
        self.gridLayout_8.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_81 = QLabel(self.groupBox_4)
        self.label_81.setFrameShape(QFrame.NoFrame)
        self.label_81.setFrameShadow(QFrame.Plain)
        self.label_81.setLineWidth(1)
        self.label_81.setMidLineWidth(0)
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.gridLayout_8.addWidget(self.label_81, 2, 2, 1, 1)
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_83 = QLabel(self.groupBox_4)
        self.label_83.setFrameShape(QFrame.NoFrame)
        self.label_83.setFrameShadow(QFrame.Plain)
        self.label_83.setLineWidth(1)
        self.label_83.setMidLineWidth(0)
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.gridLayout_8.addWidget(self.label_83, 0, 2, 1, 1)
        self.textEdit_28 = QTextEdit(self.groupBox_4)
        self.textEdit_28.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_28.setObjectName("textEdit_28")
        self.gridLayout_8.addWidget(self.textEdit_28, 2, 1, 1, 1)
        self.textEdit_27 = QTextEdit(self.groupBox_4)
        self.textEdit_27.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_27.setObjectName("textEdit_27")
        self.gridLayout_8.addWidget(self.textEdit_27, 1, 1, 1, 1)
        self.textEdit_26 = QTextEdit(self.groupBox_4)
        self.textEdit_26.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_26.setObjectName("textEdit_26")
        self.gridLayout_8.addWidget(self.textEdit_26, 0, 1, 1, 1)
        self.label_87 = QLabel(self.groupBox_4)
        self.label_87.setObjectName("label_87")
        self.gridLayout_8.addWidget(self.label_87, 2, 4, 1, 1)
        self.label_85 = QLabel(self.groupBox_4)
        self.label_85.setObjectName("label_85")
        self.gridLayout_8.addWidget(self.label_85, 0, 4, 1, 1)
        self.label_86 = QLabel(self.groupBox_4)
        self.label_86.setObjectName("label_86")
        self.gridLayout_8.addWidget(self.label_86, 1, 4, 1, 1)
        self.textEdit_63 = QTextEdit(self.groupBox_4)
        self.textEdit_63.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_63.setObjectName("textEdit_63")
        self.gridLayout_8.addWidget(self.textEdit_63, 2, 3, 1, 1)
        self.textEdit_61 = QTextEdit(self.groupBox_4)
        self.textEdit_61.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_61.setObjectName("textEdit_61")
        self.gridLayout_8.addWidget(self.textEdit_61, 0, 3, 1, 1)
        self.textEdit_62 = QTextEdit(self.groupBox_4)
        self.textEdit_62.setMaximumSize(QtCore.QSize(50, 31))
        self.textEdit_62.setObjectName("textEdit_62")
        self.gridLayout_8.addWidget(self.textEdit_62, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 4, 2, 1, 1)
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_29 = QLabel(self.groupBox_5)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 0, 0, 1, 1)
        self.textEdit_29 = QTextEdit(self.groupBox_5)
        self.textEdit_29.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_29.setObjectName("textEdit_29")
        self.gridLayout_3.addWidget(self.textEdit_29, 0, 1, 1, 1)
        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 2, 0, 1, 1)
        self.textEdit_30 = QTextEdit(self.groupBox_5)
        self.textEdit_30.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_30.setObjectName("textEdit_30")
        self.gridLayout_3.addWidget(self.textEdit_30, 2, 1, 1, 1)
        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 5, 0, 1, 1)
        self.textEdit_31 = QTextEdit(self.groupBox_5)
        self.textEdit_31.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_31.setObjectName("textEdit_31")
        self.gridLayout_3.addWidget(self.textEdit_31, 5, 1, 1, 1)
        self.label_65 = QLabel(self.groupBox_5)
        self.label_65.setObjectName("label_65")
        self.gridLayout_3.addWidget(self.label_65, 0, 2, 1, 1)
        self.textEdit_32 = QTextEdit(self.groupBox_5)
        self.textEdit_32.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_32.setObjectName("textEdit_32")
        self.gridLayout_3.addWidget(self.textEdit_32, 4, 1, 1, 1)
        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 4, 0, 1, 1)
        self.label_66 = QLabel(self.groupBox_5)
        self.label_66.setObjectName("label_66")
        self.gridLayout_3.addWidget(self.label_66, 4, 2, 1, 1)
        self.label_67 = QLabel(self.groupBox_5)
        self.label_67.setObjectName("label_67")
        self.gridLayout_3.addWidget(self.label_67, 5, 2, 1, 1)
        self.label_68 = QLabel(self.groupBox_5)
        self.label_68.setObjectName("label_68")
        self.gridLayout_3.addWidget(self.label_68, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 1, 2, 1, 1)
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit_7 = QTextEdit(self.groupBox_2)
        self.textEdit_7.setMinimumSize(QtCore.QSize(151, 0))
        self.textEdit_7.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_7.addWidget(self.textEdit_7, 0, 1, 1, 1)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_79 = QLabel(self.groupBox_2)
        self.label_79.setObjectName("label_79")
        self.gridLayout_7.addWidget(self.label_79, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 1)
        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setCheckable(True)
        self.groupBox_8.setChecked(False)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit_51 = QTextEdit(self.groupBox_8)
        self.textEdit_51.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_51.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_51.setObjectName("textEdit_51")
        self.gridLayout_6.addWidget(self.textEdit_51, 0, 1, 1, 1)
        self.textEdit_53 = QTextEdit(self.groupBox_8)
        self.textEdit_53.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_53.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_53.setObjectName("textEdit_53")
        self.gridLayout_6.addWidget(self.textEdit_53, 2, 1, 1, 1)
        self.textEdit_52 = QTextEdit(self.groupBox_8)
        self.textEdit_52.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_52.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_52.setObjectName("textEdit_52")
        self.gridLayout_6.addWidget(self.textEdit_52, 1, 1, 1, 1)
        self.label_51 = QLabel(self.groupBox_8)
        self.label_51.setObjectName("label_51")
        self.gridLayout_6.addWidget(self.label_51, 0, 0, 1, 1)
        self.label_53 = QLabel(self.groupBox_8)
        self.label_53.setObjectName("label_53")
        self.gridLayout_6.addWidget(self.label_53, 2, 0, 1, 1)
        self.label_76 = QLabel(self.groupBox_8)
        self.label_76.setObjectName("label_76")
        self.gridLayout_6.addWidget(self.label_76, 0, 2, 1, 1)
        self.label_52 = QLabel(self.groupBox_8)
        self.label_52.setObjectName("label_52")
        self.gridLayout_6.addWidget(self.label_52, 1, 0, 1, 1)
        self.label_77 = QLabel(self.groupBox_8)
        self.label_77.setObjectName("label_77")
        self.gridLayout_6.addWidget(self.label_77, 1, 2, 1, 1)
        self.label_78 = QLabel(self.groupBox_8)
        self.label_78.setObjectName("label_78")
        self.gridLayout_6.addWidget(self.label_78, 2, 2, 1, 1)
        self.textEdit_64 = QTextEdit(self.groupBox_8)
        self.textEdit_64.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_64.setObjectName("textEdit_64")
        self.gridLayout_6.addWidget(self.textEdit_64, 4, 1, 1, 1)
        self.label_94 = QLabel(self.groupBox_8)
        self.label_94.setObjectName("label_94")
        self.gridLayout_6.addWidget(self.label_94, 4, 2, 1, 1)
        self.label_95 = QLabel(self.groupBox_8)
        self.label_95.setObjectName("label_95")
        self.gridLayout_6.addWidget(self.label_95, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_8, 7, 4, 2, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 2, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 1)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_75 = QLabel(self.groupBox_7)
        self.label_75.setObjectName("label_75")
        self.gridLayout_5.addWidget(self.label_75, 0, 2, 1, 1)
        self.label_84 = QLabel(self.groupBox_7)
        self.label_84.setObjectName("label_84")
        self.gridLayout_5.addWidget(self.label_84, 1, 2, 1, 1)
        self.textEdit_50 = QTextEdit(self.groupBox_7)
        self.textEdit_50.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_50.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_50.setObjectName("textEdit_50")
        self.gridLayout_5.addWidget(self.textEdit_50, 2, 1, 1, 1)
        self.label_48 = QLabel(self.groupBox_7)
        self.label_48.setObjectName("label_48")
        self.gridLayout_5.addWidget(self.label_48, 0, 0, 1, 1)
        self.textEdit_49 = QTextEdit(self.groupBox_7)
        self.textEdit_49.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_49.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_49.setObjectName("textEdit_49")
        self.gridLayout_5.addWidget(self.textEdit_49, 1, 1, 1, 1)
        self.textEdit_48 = QTextEdit(self.groupBox_7)
        self.textEdit_48.setMinimumSize(QtCore.QSize(151, 31))
        self.textEdit_48.setMaximumSize(QtCore.QSize(151, 31))
        self.textEdit_48.setObjectName("textEdit_48")
        self.gridLayout_5.addWidget(self.textEdit_48, 0, 1, 1, 1)
        self.label_49 = QLabel(self.groupBox_7)
        self.label_49.setObjectName("label_49")
        self.gridLayout_5.addWidget(self.label_49, 1, 0, 1, 1)
        self.label_50 = QLabel(self.groupBox_7)
        self.label_50.setObjectName("label_50")
        self.gridLayout_5.addWidget(self.label_50, 2, 0, 1, 1)
        self.label_74 = QLabel(self.groupBox_7)
        self.label_74.setObjectName("label_74")
        self.gridLayout_5.addWidget(self.label_74, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 4, 4, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.consoletext = QTextEdit()
        self.consoletext.setMaximumHeight(120)
        self.consoletext.setMinimumHeight(120)
        self.MainLayout.addWidget(self.consoletext)
        self.commandLinkButton = QCommandLinkButton()
        self.MainLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.figure = figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.toolbar)

        self.verticalLayout1 = QVBoxLayout(self.tab_4)
        self.verticalLayout1.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.figure1 = figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.verticalLayout1.addWidget(self.canvas1)
        self.verticalLayout1.addWidget(self.toolbar1)

        self.verticalLayout2 = QVBoxLayout(self.tab_5)
        self.verticalLayout2.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.figure2 = figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.verticalLayout2.addWidget(self.canvas2)
        self.verticalLayout2.addWidget(self.toolbar2)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа расчёта параметров программы движения РКН методом целенаправленного поиска"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Массовые характеристики"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3425</p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">332700</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "m 2 ступ"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">89300</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "m 1 ступ"))
        self.label_8.setText(_translate("MainWindow", "m KA"))
        self.textEdit_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "m РКН"))
        self.label_88.setText(_translate("MainWindow", "кг"))
        self.label_89.setText(_translate("MainWindow", "кг"))
        self.label_90.setText(_translate("MainWindow", "кг"))
        self.label_91.setText(_translate("MainWindow", "кг"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Точность определения величин"))
        self.textEdit_55.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.001</p></body></html>"))
        self.textEdit_54.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "по Tetta"))
        self.label_54.setText(_translate("MainWindow", "по V"))
        self.label_92.setText(_translate("MainWindow", "град"))
        self.label_93.setText(_translate("MainWindow", "м/сек"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Продолжительрость работы ДУ"))
        self.label_44.setText(_translate("MainWindow", "T"))
        self.textEdit_44.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_45.setText(_translate("MainWindow", "Tk1"))
        self.textEdit_45.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">145</p></body></html>"))
        self.label_46.setText(_translate("MainWindow", "Tk2"))
        self.textEdit_47.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">430</p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "Tk3"))
        self.textEdit_46.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">285</p></body></html>"))
        self.label_69.setText(_translate("MainWindow", "сек"))
        self.label_70.setText(_translate("MainWindow", "сек"))
        self.label_71.setText(_translate("MainWindow", "сек"))
        self.label_72.setText(_translate("MainWindow", "сек"))
        self.groupBox.setTitle(_translate("MainWindow", "Первая ступень"))
        self.label.setText(_translate("MainWindow", "P"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7400000</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Sa"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.57</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "mc"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2060</p></body></html>"))
        self.label_61.setText(_translate("MainWindow", "Н"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Sm"))
        self.label_62.setText(_translate("MainWindow", "м2"))
        self.label_63.setText(_translate("MainWindow", "кг/сек"))
        self.label_64.setText(_translate("MainWindow", "м2"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Предел изменения параметров"))
        self.label_82.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "по alfa"))
        self.label_81.setText(_translate("MainWindow", "-"))
        self.label_27.setText(_translate("MainWindow", "по tet1"))
        self.label_28.setText(_translate("MainWindow", "по tet2"))
        self.label_83.setText(_translate("MainWindow", "-"))
        self.textEdit_28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textEdit_27.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textEdit_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-2</p></body></html>"))
        self.label_87.setText(_translate("MainWindow", "град/сек"))
        self.label_85.setText(_translate("MainWindow", "град"))
        self.label_86.setText(_translate("MainWindow", "град/сек"))
        self.textEdit_63.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-0.4</p></body></html>"))
        self.textEdit_61.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-4</p></body></html>"))
        self.textEdit_62.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-0.4</p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Втораая ступень"))
        self.label_29.setText(_translate("MainWindow", "P"))
        self.textEdit_29.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">912000</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "Sa"))
        self.textEdit_30.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.9</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "mc"))
        self.textEdit_31.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">260</p></body></html>"))
        self.label_65.setText(_translate("MainWindow", "Н"))
        self.textEdit_32.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Sm"))
        self.label_66.setText(_translate("MainWindow", "м2"))
        self.label_67.setText(_translate("MainWindow", "кг/сек"))
        self.label_68.setText(_translate("MainWindow", "м2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Шаг перебора"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-0.1</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "по alfa"))
        self.label_79.setText(_translate("MainWindow", "град"))
        self.groupBox_8.setTitle(_translate("MainWindow", "ДУ малой тяги"))
        self.textEdit_51.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">80000</p></body></html>"))
        self.textEdit_53.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23</p></body></html>"))
        self.textEdit_52.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_51.setText(_translate("MainWindow", "P"))
        self.label_53.setText(_translate("MainWindow", "mc"))
        self.label_76.setText(_translate("MainWindow", "Н"))
        self.label_52.setText(_translate("MainWindow", "Sa"))
        self.label_77.setText(_translate("MainWindow", "м2"))
        self.label_78.setText(_translate("MainWindow", "кг/сек"))
        self.textEdit_64.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">44</p></body></html>"))
        self.label_94.setText(_translate("MainWindow", "сек"))
        self.label_95.setText(_translate("MainWindow", "Длительность"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Текущее значение параметров"))
        self.label_75.setText(_translate("MainWindow", "град"))
        self.label_84.setText(_translate("MainWindow", "град/сек"))
        self.textEdit_50.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_48.setText(_translate("MainWindow", "alfa"))
        self.textEdit_49.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textEdit_48.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_49.setText(_translate("MainWindow", "tet1"))
        self.label_50.setText(_translate("MainWindow", "tet2"))
        self.label_74.setText(_translate("MainWindow", "град/сек"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Исходные данные"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Угол наклона вектора скорости"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Угол тангажа"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Высота"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Графики"))
        self.commandLinkButton.setText(_translate("MainWindow", "Рассчитать"))

