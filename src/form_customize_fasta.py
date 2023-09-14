# Implementation of GUI form for choice of desired FASTA files with 2 AA sequences for alignment

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_customize_fasta.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QFile, QIODevice)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
                               QWidget, QMainWindow, QFileDialog, QListWidget, QMessageBox, QCheckBox, QComboBox)

from alignments_lotos import *
from form_tekstualni_izvestaj_poravnanja import *

# utility function for name compression
def decrease_name_size(name):
    ind = name.rindex('|')
    s = name[ind+1:]
    print(s)
    rind = s.find(' ')
    print(s[:rind])
    return s[:rind]


# class for UI form for choice FASTA files with AA sequences of desired proteins
class Ui_Form(QWidget):
    fastaFilePaths = []

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(446, 329)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget()
        self.listWidget.setObjectName(u"listWidget")
        # self.textEdit = QTextEdit(Form)
        # self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.listWidget)
        #self.verticalLayout.addWidget(self.textEdit)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.checkBoxGlobalno = QCheckBox()
        self.checkBoxGlobalno.setObjectName(u"checkBoxGlobalno")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.checkBoxGlobalno)

        self.checkBoxLokalno = QCheckBox()
        self.checkBoxLokalno.setObjectName(u"checkBoxLokalno")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.checkBoxLokalno)
        self.labelKaznaOtvaranja = QLabel(Form)
        self.labelKaznaOtvaranja.setObjectName(u"labelKaznaOtvaranja")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.labelKaznaOtvaranja)

        self.comboBoxKaznaOtvaranja = QComboBox(Form)
        self.comboBoxKaznaOtvaranja.addItem("1")
        self.comboBoxKaznaOtvaranja.addItem("5")
        self.comboBoxKaznaOtvaranja.addItem("10")
        self.comboBoxKaznaOtvaranja.addItem("15")
        self.comboBoxKaznaOtvaranja.addItem("25")
        self.comboBoxKaznaOtvaranja.addItem("50")
        self.comboBoxKaznaOtvaranja.addItem("100")
        self.comboBoxKaznaOtvaranja.setCurrentIndex(2)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBoxKaznaOtvaranja)

        self.labelKaznaNastavka = QLabel(Form)
        self.labelKaznaNastavka.setObjectName(u"labelKaznaNastavka")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.labelKaznaNastavka)

        self.comboBoxKaznaNastavka = QComboBox(Form)
        self.comboBoxKaznaNastavka.addItem("0")
        self.comboBoxKaznaNastavka.addItem("1")
        self.comboBoxKaznaNastavka.addItem("5")
        self.comboBoxKaznaNastavka.addItem("10")

        self.comboBoxKaznaNastavka.setCurrentIndex(0)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBoxKaznaNastavka)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)
        self.setWindowTitle("Ucitavanje aminokiselinskih sekvenci")
        self.pushButton.clicked.connect(self.otvoriClicked)
        self.pushButton_2.clicked.connect(self.omotacIzvrsiPoravnanje)

        self.fastaFilePaths = []
        self.windowAlignmentReport = WidgetIzvestajPoravnanja()

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Izaberi FASTA datoteke sekvenci", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Broj ucitanih datoteka:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.checkBoxGlobalno.setText(QCoreApplication.translate("Form", u"Globalno poravnanje", None))
        self.checkBoxLokalno.setText(QCoreApplication.translate("Form", u"Lokalno poravnanje", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Otvori novu datoteku", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Izvrsi poravnanje", None))
        self.labelKaznaOtvaranja.setText(QCoreApplication.translate("Form", u"Kazna za otvaranje prazine:", None))
        self.labelKaznaNastavka.setText(QCoreApplication.translate("Form", u"Kazna za nastavljanje prazina:", None))
    # retranslateUi

    def clearContent(self):
        self.fastaFilePaths.clear()
        self.listWidget.clear()
        self.label_3.setText("0")

    def otvoriClicked(self):
        fastaFileName = QFileDialog.getOpenFileName(self)[0]
        self.fastaFilePaths.append(fastaFileName)
        fileContent = ""
        fastaFile = QFile(fastaFileName)
        fastaFile.open(QIODevice.ReadOnly)

        while not fastaFile.atEnd():
            fileContent += fastaFile.readLine()

        # text = self.textEdit.toPlainText()
        # self.textEdit.setText(text + fileContent)
        self.listWidget.addItem(fileContent)
        self.label_3.setText(str(int(self.label_3.text())+1))

    def omotacIzvrsiPoravnanje(self):
        '''if int(self.label_3.text()) < 2:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Nedovoljno ucitanih sekvenci")
            msgBox.setText("Ucitaj sekvence za poravnanje")
            msgBox.exec()
            return'''

        if not self.checkBoxLokalno.isChecked() and not self.checkBoxGlobalno.isChecked():
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Nije izabrana vrsta poravnanja")
            msgBox.setText("Izaberi vrstu poravnanja (lokalno ili globalno poravnanje)")
            msgBox.exec()
            return

        if self.checkBoxLokalno.isChecked() and self.checkBoxGlobalno.isChecked():
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ne mogu obe vrste poravnanja")
            msgBox.setText("Izaberi tacno jednu vrstu poravnanja (lokalno ili globalno poravnanje)")
            msgBox.exec()
            return

        print("Vrsimo poravnanje 2 aa sekvence")
        open_penalty = -int(self.comboBoxKaznaOtvaranja.currentText())
        continue_penalty = -int(self.comboBoxKaznaNastavka.currentText())
        lines = []
        aligns = []
        labels = []
        if self.checkBoxLokalno.isChecked():
            result = execute_alignment_and_generate_report(self.fastaFilePaths, type_a='l', open_penalty=open_penalty, continue_penalty=continue_penalty)
            aligns = result[1]
            lines += result[2]
            labels = result[0]

        elif self.checkBoxGlobalno.isChecked():
            result = execute_alignment_and_generate_report(self.fastaFilePaths, type_a='g', open_penalty=open_penalty, continue_penalty=continue_penalty)
            aligns = result[1]
            lines += result[2]
            labels = result[0]

        self.windowAlignmentReport.clearContent()
        self.windowAlignmentReport.setAlignments(aligns)
        self.windowAlignmentReport.setReportLines(lines)
        self.windowAlignmentReport.setLabels(labels)

        for line in lines:
            self.windowAlignmentReport.ui.list_Izvestaj.addItem(line)

        self.windowAlignmentReport.show()


# class for window whose UI is implemented class above
class Widget_Fasta(QWidget):
    def __init__(self):
        super(Widget_Fasta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Ucitavanje aminokiselinskih sekvenci")

    def clearContent(self):
        self.ui.clearContent()
