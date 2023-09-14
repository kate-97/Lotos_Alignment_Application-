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
                               QSizePolicy, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QComboBox)
from form_tekstualni_izvestaj_poravnanja import *
import load_pb_data as lpb
import alignments_lotos_pb
from form_tekstualni_izvestaj_poravnanja import *


# class for UI form for input of two PDB-s of desired proteins
class Ui_Form_2_pdb(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 590)
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

        self.pushButtonAddFile = QPushButton(Form)
        self.pushButtonAddFile.setObjectName(u"pushButtonAddFile")

        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.pushButtonAddPDB)
        self.verticalLayout.addWidget(self.pushButtonAddFile)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_Counter = QLabel(Form)
        self.label_Counter.setObjectName(u"label_Counter")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_Counter)

        self.groupBox_ = QGroupBox(Form)
        self.groupBox_.setObjectName(u"groupBox")
        self.horizontal_Layout = QHBoxLayout(self.groupBox_)
        self.horizontal_Layout.setObjectName(u"horizontalLayout")
        self.rb_lokalno = QRadioButton(self.groupBox_)
        self.rb_lokalno.setObjectName(u"rb_lokalno")

        self.horizontal_Layout.addWidget(self.rb_lokalno)

        self.rb_globalno = QRadioButton(self.groupBox_)
        self.rb_globalno.setObjectName(u"rb_globalno")

        self.horizontal_Layout.addWidget(self.rb_globalno)
        self.verticalLayout.addWidget(self.groupBox_)


        self.labelDodatnaPodesavanja = QLabel(Form)
        self.labelDodatnaPodesavanja.setObjectName(u"label_DodatnaPodesavanja")
        self.verticalLayout.addWidget(self.labelDodatnaPodesavanja)


        self.formLayout2 = QFormLayout()

        self.labelKaznaOtvaranja = QLabel(Form)
        self.labelKaznaOtvaranja.setObjectName(u"labelKaznaOtvaranja")

        self.formLayout2.setWidget(0, QFormLayout.LabelRole, self.labelKaznaOtvaranja)

        self.comboBoxKaznaOtvaranja = QComboBox(Form)
        self.comboBoxKaznaOtvaranja.addItem("1")
        self.comboBoxKaznaOtvaranja.addItem("5")
        self.comboBoxKaznaOtvaranja.addItem("10")
        self.comboBoxKaznaOtvaranja.addItem("15")
        self.comboBoxKaznaOtvaranja.addItem("25")
        self.comboBoxKaznaOtvaranja.addItem("50")
        self.comboBoxKaznaOtvaranja.addItem("100")
        self.comboBoxKaznaOtvaranja.setCurrentIndex(2)

        self.formLayout2.setWidget(0, QFormLayout.FieldRole, self.comboBoxKaznaOtvaranja)

        self.labelKaznaNastavka = QLabel(Form)
        self.labelKaznaNastavka.setObjectName(u"labelKaznaNastavka")

        self.formLayout2.setWidget(1, QFormLayout.LabelRole, self.labelKaznaNastavka)

        self.comboBoxKaznaNastavka = QComboBox(Form)
        self.comboBoxKaznaNastavka.addItem("0")
        self.comboBoxKaznaNastavka.addItem("1")
        self.comboBoxKaznaNastavka.addItem("5")
        self.comboBoxKaznaNastavka.addItem("10")

        self.comboBoxKaznaNastavka.setCurrentIndex(0)

        self.formLayout2.setWidget(1, QFormLayout.FieldRole, self.comboBoxKaznaNastavka)

        self.verticalLayout.addLayout(self.formLayout2)


        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout3 = QHBoxLayout()
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.horizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout3.addItem(self.horizontalSpacer)
        self.pb_ocisti = QPushButton(Form)
        self.pb_ocisti.setObjectName(u"pb_ocisti")
        self.horizontalLayout3.addWidget(self.pb_ocisti)
        self.verticalLayout.addLayout(self.horizontalLayout3)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.sources = []
        self.windowTextReport = WidgetIzvestajPoravnanja()

        self.retranslateUi(Form)
        self.pushButtonAddPDB.clicked.connect(self.onPbAddPDBClicked)
        self.pushButtonAddFile.clicked.connect(self.onPbAddFileClicked)
        self.pushButton.clicked.connect(self.onPbClicked)
        self.pb_ocisti.clicked.connect(self.clearContent)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Unesite PDB ID proteina ili\nizaberite PDB/FASTA datoteku:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Broj ucitanih:", None))
        self.label_Counter.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Izvrsi poravnanje", None))
        self.pushButtonAddPDB.setText(QCoreApplication.translate("Form", u"Dodaj PDB", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("Form", u"Ucitaj datoteku", None))

        self.rb_lokalno.setText(QCoreApplication.translate("Form", u"Lokalno poravnanje", None))
        self.rb_lokalno.setChecked(True)
        self.rb_globalno.setText(QCoreApplication.translate("Form", u"Globalno poravnanje", None))
        self.labelKaznaOtvaranja.setText(QCoreApplication.translate("Form", u"Kazna za otvaranje prazine:", None))
        self.labelKaznaNastavka.setText(QCoreApplication.translate("Form", u"Kazna za nastavljanje prazina:", None))
        self.labelDodatnaPodesavanja.setText(QCoreApplication.translate("Form", u"Dodatna podesavanja parametara", None))
        self.pb_ocisti.setText(QCoreApplication.translate("Form", u"Ocisti", None))
    # retranslateUi

    def onPbAddPDBClicked(self):
        pdb_id = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem("(PDB id) " + pdb_id)
        self.sources.append((pdb_id, "id"))
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
        self.sources = lpb.generate_fastas(self.sources)

        open_penalty = -int(self.comboBoxKaznaOtvaranja.currentText())
        continue_penalty = -int(self.comboBoxKaznaNastavka.currentText())

        if self.rb_lokalno.isChecked():
            alignment_results = alignments_lotos_pb.execute_alignment_and_generate_report(self.sources, type_a="l", open_penalty=open_penalty, continue_penalty=continue_penalty)
        else:
            alignment_results = alignments_lotos_pb.execute_alignment_and_generate_report(self.sources, type_a="g", open_penalty=open_penalty, continue_penalty=continue_penalty)

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


    def onPbAddFileClicked(self):
        newFile = QFileDialog.getOpenFileName(self)[0]
        newFile_s = ''
        pos = newFile.rfind('/')

        if pos == -1:
            newFile_s =newFile

        else:
            newFile_s = newFile[pos + 1:]

        if newFile.endswith(".pdb") or newFile.endswith(".PDB"):
            self.listWidget.addItem("(pdb file) " + newFile_s)
            self.sources.append((newFile, "pdb"))

        else:
            self.listWidget.addItem("(fasta file) " + newFile_s)
            self.sources.append((newFile, "fasta"))

        countPdb = int(self.label_Counter.text())
        countPdb += 1
        self.label_Counter.setText(str(countPdb))


    def clearContent(self):
        self.listWidget.clear()
        self.sources = []
        self.label_Counter.setText("0")
        self.comboBoxKaznaOtvaranja.setCurrentIndex(2)
        self.comboBoxKaznaNastavka.setCurrentIndex(0)
        self.rb_lokalno.setChecked(True)


# class for window whose UI is implemented class above
class Widget2PDB(QWidget):
    def __init__(self):
        super(Widget2PDB, self).__init__()
        self.ui = Ui_Form_2_pdb()
        self.ui.setupUi(self)
        self.setWindowTitle("Ucitavanje PDB datoteka ili PB sekvenci u FASTA formatu")

    def clearContent(self):
        self.ui.clearContent()

