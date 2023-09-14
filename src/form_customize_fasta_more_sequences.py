# Implementation of GUI form for choice of desired FASTA files with more AA sequences for multiple alignment

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
                               QWidget, QMainWindow, QFileDialog, QListWidget, QMessageBox, QCheckBox)
from form_tekstualni_izvestaj_visestrukog_poravnanja import *
from multiple_alignments_lotos import *


# utility function for name compression
def decrease_name_size(name):
    ind = name.rindex('|')
    s = name[ind+1:]
    print(s)
    dind = s.find(' ')
    print(s[:dind])
    return s[:dind]


# class for UI form for choice FASTA files with AA sequences of desired proteins
class Ui_Form_more_sequences(QWidget):
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

        self.fastaFilePaths = []
        self.windowAlignmentReport = WidgetIzvestajVisestrukogPoravnanja()

        self.retranslateUi(Form)
        self.setWindowTitle("Ucitavanje aminokiselinskih sekvenci")
        self.pushButton.clicked.connect(self.otvoriClicked)
        self.pushButton_2.clicked.connect(self.omotacIzvrsiPoravnanje)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def clearContent(self):
        self.listWidget.clear()
        self.label_3.setText("0")
        self.fastaFilePaths.clear()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Izaberi FASTA datoteke sekvenci", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Broj ucitanih sekvenci:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Otvori novu datoteku", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Izvrsi poravnanje", None))
    # retranslateUi

    def otvoriClicked(self):
        fastaFileName = QFileDialog.getOpenFileName(self)[0]
        fileContent = ""
        fastaFile = QFile(fastaFileName)
        fastaFile.open(QIODevice.ReadOnly)
        self.fastaFilePaths.append(fastaFileName)

        while not fastaFile.atEnd():
            fileContent += fastaFile.readLine()

        # text = self.textEdit.toPlainText()
        # self.textEdit.setText(text + fileContent)
        self.listWidget.addItem(fileContent)
        self.label_3.setText(str(int(self.label_3.text())+1))

    def omotacIzvrsiPoravnanje(self):
        if int(self.label_3.text()) < 2:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Nedovoljno ucitanih sekvenci")
            msgBox.setText("Ucitaj sekvence za poravnanje")
            msgBox.exec()
            return

        print("Vrsimo poravnanje vise aa sekvence")
        labels, alignment_data, lines = execute_alignment_and_generate_report(self.fastaFilePaths)
        self.windowAlignmentReport.clearContent()
        self.windowAlignmentReport.set_alignment_data(alignment_data)
        self.windowAlignmentReport.setReportLines(lines)
        self.windowAlignmentReport.set_labels([decrease_name_size(l) for l in labels])
        print(labels)
        for line in lines:
            self.windowAlignmentReport.ui.list_Izvestaj.addItem(line)

        self.windowAlignmentReport.show()


# class for window whose UI is implemented class above
class WidgetMoreSequences(QWidget):
    def __init__(self):
        super(WidgetMoreSequences, self).__init__()
        self.ui = Ui_Form_more_sequences()
        self.ui.setupUi(self)
        self.setWindowTitle("Ucitavanje aminokiselinskih sekvenci")

    def clearContent(self):
        self.ui.clearContent()