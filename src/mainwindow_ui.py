# Implementation of GUI of the application main window

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

from form_customize_fasta import *
import form_customize_fasta as fa
from form_customize_fasta_more_sequences import *
from form_customize_2_pdb import *
from form_customize_more_pdb import *
import os
from alignments_lotos import *


# MainWindow class
# FIXME: Names of action functions are on serbian language
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 460)
        MainWindow.setMaximumSize(QSize(500, 460))
        self.actionDve_aminokiselinske_sekvence = QAction(MainWindow, self)
        self.actionDve_aminokiselinske_sekvence.setObjectName(u"actionDve_aminokiselinske_sekvence")
        self.actionDve_aminokiselinske_sekvence.triggered.connect(self.poravnanje_dve_aa_sekvence)
        self.actionDve_PB_sekvence = QAction(MainWindow)
        self.actionDve_PB_sekvence.setObjectName(u"actionDve_PB_sekvence")
        self.actionDve_PB_sekvence.triggered.connect(self.poravnanje_dve_pb_sekvence)
        self.actionVise_AA_sekvenci = QAction(MainWindow, self)
        self.actionVise_AA_sekvenci.setObjectName(u"actionVise_AA_sekvenci")
        self.actionVise_AA_sekvenci.triggered.connect(self.poravnanje_vise_aa_sekvenci)
        self.actionVise_PB_sekvenci = QAction(MainWindow, self)
        self.actionVise_PB_sekvenci.setObjectName(u"actionVise_PB_sekvenci")
        self.actionVise_PB_sekvenci.triggered.connect(self.poravnanje_vise_pb_sekvenci)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.applicationLogo = QLabel(self.centralwidget)
        self.applicationLogo.setObjectName(u"applicationLogo")
        self.applicationLogo.setPixmap(QPixmap(u"../Images/lotosLogo.png"))

        self.verticalLayout.addWidget(self.applicationLogo)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 24))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(13, 0, 160, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 217))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(48, 44, 139, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.menubar.setPalette(palette)
        self.menuIzvrsi_poravnanje = QMenu(self.menubar)
        self.menuIzvrsi_poravnanje.setObjectName(u"menuIzvrsi_poravnanje")
        self.menuGenerisi_izvestaj = QMenu(self.menubar)
        self.menuGenerisi_izvestaj.setObjectName(u"menuGenerisi_izvestaj")


        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuIzvrsi_poravnanje.menuAction())
        self.menubar.addAction(self.menuGenerisi_izvestaj.menuAction())
        self.menuIzvrsi_poravnanje.addAction(self.actionDve_aminokiselinske_sekvence)
        self.menuIzvrsi_poravnanje.addAction(self.actionDve_PB_sekvence)
        self.menuIzvrsi_poravnanje.addSeparator()
        self.menuIzvrsi_poravnanje.addAction(self.actionVise_AA_sekvenci)
        self.menuIzvrsi_poravnanje.addAction(self.actionVise_PB_sekvenci)

        self.reading_fasta_2_window = fa.Widget_Fasta()
        self.reading_fasta_more_window = WidgetMoreSequences()
        self.reading_pdb_2_window = Widget2PDB()
        self.reading_pdb_more_window = WidgetMorePDB()


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lotos", None))
        self.actionDve_aminokiselinske_sekvence.setText(QCoreApplication.translate("MainWindow", u"Dve aminokiselinske sekvence", None))
        self.actionDve_PB_sekvence.setText(QCoreApplication.translate("MainWindow", u"Dve PB sekvence", None))
        self.actionVise_AA_sekvenci.setText(QCoreApplication.translate("MainWindow", u"Vise aminokiselinskih sekvenci", None))
        self.actionVise_PB_sekvenci.setText(QCoreApplication.translate("MainWindow", u"Vise PB sekvenci", None))
        self.applicationLogo.setText("")
        self.menuIzvrsi_poravnanje.setTitle(QCoreApplication.translate("MainWindow", u"Izvrsi poravnanje", None))
        self.menuGenerisi_izvestaj.setTitle(QCoreApplication.translate("MainWindow", u"Generisi izvestaj", None))
    # retranslateUi

    def poravnanje_dve_aa_sekvence(self):
        action = self.sender()
        self.reading_fasta_2_window.clearContent()
        self.reading_fasta_2_window.show()

    def poravnanje_dve_pb_sekvence(self):
        action = self.sender()
        self.reading_pdb_2_window.clearContent()
        self.reading_pdb_2_window.show()

    def poravnanje_vise_aa_sekvenci(self):
        action = self.sender()
        self.reading_fasta_more_window.clearContent()
        self.reading_fasta_more_window.show()

    def poravnanje_vise_pb_sekvenci(self):
        action = self.sender()
        self.reading_pdb_more_window.clearContent()
        self.reading_pdb_more_window.show()
