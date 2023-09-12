# Implementation of GUI form for input desired PDB-s for alignment of two PB sequences

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_customize_pdb.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget, QMessageBox)
from form_tekstualni_izvestaj_poravnanja import *
import load_pb_data as lpb
import alignments_lotos_pb
from form_tekstualni_izvestaj_poravnanja import *


# class for UI form for input of two PDB-s of desired proteins
class Ui_Form_2_pdb(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(308, 314)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(1000, 500))

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.pushButtonAddPDB = QPushButton(Form)
        self.pushButtonAddPDB.setObjectName(u"pushButtonAddPDB")

        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.pushButtonAddPDB)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_Counter = QLabel(Form)
        self.label_Counter.setObjectName(u"label_Counter")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_Counter)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pdb_ids = []
        self.windowTextReport = WidgetIzvestajPoravnanja()

        self.retranslateUi(Form)
        self.pushButtonAddPDB.clicked.connect(self.onPbAddPDBClicked)
        self.pushButton.clicked.connect(self.onPbClicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Unesite PDB ID proteina:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Broj ucitanih:", None))
        self.label_Counter.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Izvrsi poravnanje", None))
        self.pushButtonAddPDB.setText(QCoreApplication.translate("Form", u"Dodaj PDB", None))
    # retranslateUi

    def onPbAddPDBClicked(self):
        pdb_id = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem(pdb_id)
        self.pdb_ids.append(pdb_id)
        countPdb = int(self.label_Counter.text())
        countPdb += 1
        self.label_Counter.setText(str(countPdb))

    def onPbClicked(self):
        if int(self.label_Counter.text()) < 2:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Nedovoljno ucitanih sekvenci")
            msgBox.setText("Ucitaj sekvence za poravnanje")
            msgBox.exec()
            return

        print("Vrsimo poravnanje 2 pb sekvence")
        alignment_results = alignments_lotos_pb.load_pbs_and_execute_pairwise_alignment_with_report(pdbs = self.pdb_ids)
        if alignment_results is None:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Neispravna sekvenca")
            msgBox.setText("Jedan ili vise proteina su nekompletni, pa ne mogu biti poravnati sa drugim proteinima.")
            msgBox.exec()
            return

        labels = alignment_results[0]
        alignments = alignment_results[1]
        lines = alignment_results[2]

        self.windowTextReport.clearContent()
        self.windowTextReport.setLabels(labels)
        self.windowTextReport.setAlignments(alignments)
        self.windowTextReport.setReportLines(lines)

        for line in lines:
            self.windowTextReport.ui.list_Izvestaj.addItem(line)

        self.windowTextReport.show()  # TODO Postoji problem sa razmacima

    def clearContent(self):
        self.listWidget.clear()
        self.pdb_ids.clear()
        self.label_Counter.setText("0")


# class for window whose UI is implemented class above
class Widget2PDB(QWidget):
    def __init__(self):
        super(Widget2PDB, self).__init__()
        self.ui = Ui_Form_2_pdb()
        self.ui.setupUi(self)
        self.setWindowTitle("Ucitavanje aminokiselinskih sekvenci")

    def clearContent(self):
        self.ui.clearContent()

