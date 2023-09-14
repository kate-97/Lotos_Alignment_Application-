# Implementation of GUI form for display of textual report of multiple alignment. (both of AA and PB sequences).
# Contains member fields for storing alignment data which might be used for visualisations.

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_tekstualni_izvestaj_poravnanja.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import graphical_reports_alignment_lotos as gl
import datetime
from window_izbor_msa_vizuelizacije import *



# class for UI for display of textual report of multiple alignment (both for AA and PB sequences)
# contains member fields in which are stored alignment data which might be used later for visualisations
# FIXME: Name of class and member function is on serbian language.
class Ui_Form_Izvestaj_Visestrukog_Poravnanja(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(827, 495)
        palette = QPalette()
        brush = QBrush(QColor(35, 137, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        Form.setPalette(palette)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.list_Izvestaj = QListWidget(Form)
        self.list_Izvestaj.setObjectName(u"list_Izvestaj")

        self.verticalLayout.addWidget(self.list_Izvestaj)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.pb_sacuvaj_tekst = QPushButton(Form)

        self.pb_vizuelizacija = QPushButton(Form)
        self.pb_vizuelizacija.setObjectName(u"pb_vizuelizacija")

        self.horizontalLayout.addWidget(self.pb_vizuelizacija)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_sacuvaj_tekst.setObjectName(u"pb_sacuvaj_tekst")

        self.horizontalLayout.addWidget(self.pb_sacuvaj_tekst)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)
        self.labels = None # TODO
        self.alignment_data = None
        self.reportLines = None
        self.windowViz = WidgetMSAVizuelizacija()

        self.pb_sacuvaj_tekst.clicked.connect(self.clickPbSacuvajTekst)
        self.pb_vizuelizacija.clicked.connect(self.clickPbVizuelizacija)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tekstualni izvestaj dobijenog poravnanja", None))
        self.pb_sacuvaj_tekst.setText(QCoreApplication.translate("Form", u"Sacuvaj tekstualni izvestaj", None))
        self.pb_vizuelizacija.setText(QCoreApplication.translate("Form", u"Generisi vizuelizaciju", None))
    # retranslateUi

    def clearContent(self):
        self.list_Izvestaj.clear()
        self.alignments = None
        self.reportLines = None
        self.labels = None


    def set_labels(self, labels):
        self.labels = labels

    def set_alignment_data(self, alignment_data):
        self.alignment_data = alignment_data

    def setReportLines(self, lines):
        self.reportLines = lines

    def clickPbSacuvajTekst(self):
        file_name = "alignment_report__" + str(datetime.date.today()) + "__" + str(datetime.datetime.now().hour) \
                    + "_" + str(datetime.datetime.now().minute) + ".txt"
        f = open(file_name, 'w')

        for line in self.reportLines:
            f.write(line + "\n")

        f.flush()
        f.close()
        print('Report wrote in file ' + file_name, file=sys.stderr)

    def clickPbVizuelizacija(self):
        self.windowViz.ocisti_izbor()
        self.windowViz.set_alignment_data(self.alignment_data)
        self.windowViz.set_labels(self.labels)
        self.windowViz.show()


# class for window whose UI is implemented class above
class WidgetIzvestajVisestrukogPoravnanja(QWidget):
    def __init__(self):
        super(WidgetIzvestajVisestrukogPoravnanja, self).__init__()
        self.ui = Ui_Form_Izvestaj_Visestrukog_Poravnanja()
        self.ui.setupUi(self)
        self.setWindowTitle("Izvestaj")

    def clearContent(self):
        self.ui.clearContent()

    def set_alignment_data(self, alignment_data):
        self.ui.set_alignment_data(alignment_data)

    def setReportLines(self, lines):
        self.ui.setReportLines(lines)

    def set_labels(self, labels):
        self.ui.set_labels(labels)