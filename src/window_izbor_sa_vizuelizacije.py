# Implementation of GUI form for choice of visualisations for pairwise alignment (both of AA and PB sequences)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'izbor_sa_vizuelizacije.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import datetime
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import graphical_reports_alignment_lotos as gl


# class for UI form for choice of visualisations
# contains data about alignment for which visualisation is desired
# FIXME: Names of some functions are on Serbian language
class Ui_Form_SA_Viz(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(311, 193)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(87, 75, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.checkBox_Classic = QCheckBox(Form)
        self.checkBox_Classic.setObjectName(u"checkBox_Classic")

        self.verticalLayout.addWidget(self.checkBox_Classic)

        self.checkBox_SimilarityBased = QCheckBox(Form)
        self.checkBox_SimilarityBased.setObjectName(u"checkBox_SimilarityBased")

        self.verticalLayout.addWidget(self.checkBox_SimilarityBased)

        self.checkBox_LikeAText = QCheckBox(Form)
        self.checkBox_LikeAText.setObjectName(u"checkBox_LikeAText")

        self.verticalLayout.addWidget(self.checkBox_LikeAText)

        self.pb_Generisi = QPushButton(Form)
        self.pb_Generisi.setObjectName(u"pb_Generisi")

        self.verticalLayout.addWidget(self.pb_Generisi)

        self.labels = None
        self.alignments = []

        self.retranslateUi(Form)

        self.pb_Generisi.clicked.connect(self.pbGenerisi_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Izaberi zeljenu vizuelizaciju/vizuelizacije", None))
        self.checkBox_Classic.setText(QCoreApplication.translate("Form", u"Klasicna vizuelizacija poravnanja", None))
        self.checkBox_SimilarityBased.setText(QCoreApplication.translate("Form", u"Vizuelizacija bazirana na slicnosti", None))
        self.checkBox_LikeAText.setText(QCoreApplication.translate("Form", u"Vizuelizacija kao u tekstu", None))
        self.pb_Generisi.setText(QCoreApplication.translate("Form", u"Generisi vizuelizacije", None))
    # retranslateUi

    def pbGenerisi_clicked(self):
        if self.checkBox_Classic.isChecked():
            i = 0
            for alignment in self.alignments:
                file_name = 'graphical_report_classic_visualisation__' + str(datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '__' + str(i) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_classic_alignment_visualisation(alignment,self.labels, file_name)
                i += 1
        if self.checkBox_SimilarityBased.isChecked():
            i = 0
            for alignment in self.alignments:
                file_name = 'graphical_report_similarity_based__' + str(datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '__' + str(i) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_similarity_based_alignment_visualisation(alignment, self.labels, file_name)
                i += 1
        if self.checkBox_LikeAText.isChecked():
            i = 0
            for alignment in self.alignments:
                file_name = 'graphical_report_plt__' + str(datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '__' + str(i) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_text_alignment_view(alignment, file_name)
                i += 1

    def ocisti_izbor(self):
        self.checkBox_LikeAText.setChecked(False)
        self.checkBox_Classic.setChecked(False)
        self.checkBox_SimilarityBased.setChecked(False)
        self.alignments = []
        self.labels = None

    def set_alignments(self, alignments):
        self.alignments = alignments

    def set_labels(self, labels):
        self.labels = labels

# class for window whose UI is implemented class above
# FIXME: Names of some functions are on Serbian language
class WidgetSAVizuelizacija(QWidget):
    def __init__(self):
        super(WidgetSAVizuelizacija, self).__init__()
        self.ui = Ui_Form_SA_Viz()
        self.ui.setupUi(self)
        self.setWindowTitle("Izaberi vizuelizacije")

    def ocisti_izbor(self):
        self.ui.ocisti_izbor()

    def set_alignments(self, alignments):
        self.ui.set_alignments(alignments)

    def set_labels(self, labels):
        self.ui.set_labels(labels)

