# Implementation of GUI form for choice of desired PDB-s of desired proteins for multiple alignment

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
                               QSizePolicy, QVBoxLayout, QWidget, QMessageBox, QFileDialog)
from form_tekstualni_izvestaj_visestrukog_poravnanja import *
import multiple_alignments_lotos_pb
import load_pb_data as lpb


# class for UI form for input of PDB-s of desired proteins
class Ui_Form_more_pdb(QWidget):
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


        self.retranslateUi(Form)

        self.sources = []
        self.windowAlignmentReport = WidgetIzvestajVisestrukogPoravnanja()


        self.pushButtonAddPDB.clicked.connect(self.onPbAddPDBClicked)
        self.pushButton.clicked.connect(self.onPbClicked)
        self.pushButtonAddFile.clicked.connect(self.onPbAddFileClicked)
        self.pb_ocisti.clicked.connect(self.clearContent)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Unesite PDB ID proteina:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Broj ucitanih:", None))
        self.label_Counter.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Izvrsi poravnanje", None))
        self.pushButtonAddPDB.setText(QCoreApplication.translate("Form", u"Dodaj PDB", None))
        self.pb_ocisti.setText(QCoreApplication.translate("Form", u"Ocisti", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("Form", u"Ucitaj datoteku", None))
    # retranslateUi

    def clearContent(self):
        self.listWidget.clear()
        self.label_Counter.setText("0")
        self.sources = []

    def onPbAddPDBClicked(self):
        pdb_id = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem("(PDB id) " + pdb_id)
        self.sources.append((pdb_id, "id"))
        countPdb = int(self.label_Counter.text())
        countPdb += 1
        self.label_Counter.setText(str(countPdb))

    def onPbAddFileClicked(self):
        newFile = QFileDialog.getOpenFileName(self)[0]
        pos = newFile.rindex('/')
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

    def onPbClicked(self):
        print("Vrsimo poravnanje vise pb sekvenci")
        self.sources = lpb.generate_fastas(self.sources)

        result_ = multiple_alignments_lotos_pb.execute_alignment_and_generate_report(self.sources)
        if result_ is None:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Neispravna sekvenca")
            msgBox.setText("Jedan ili vise proteina su nekompletni, pa ne mogu biti poravnati sa drugim proteinima.")
            msgBox.exec()
            return

        labels = result_[0]
        alignment_data = result_[1]
        lines = result_[2]

        self.windowAlignmentReport.clearContent()
        self.windowAlignmentReport.set_alignment_data(alignment_data)
        self.windowAlignmentReport.setReportLines(lines)
        self.windowAlignmentReport.set_labels([multiple_alignments_lotos_pb.decrease_name_size(l) for l in labels])

        for line in lines:
            self.windowAlignmentReport.ui.list_Izvestaj.addItem(line)

        self.windowAlignmentReport.show()


# class for window whose UI is implemented class above
class WidgetMorePDB(QWidget):
    def __init__(self):
        super(WidgetMorePDB, self).__init__()
        self.ui = Ui_Form_more_pdb()
        self.ui.setupUi(self)
        self.setWindowTitle("Ucitavanje PDB datoteka ili PB sekvenci u FASTA formatu")

    def clearContent(self):
        self.ui.clearContent()
