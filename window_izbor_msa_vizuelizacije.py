# Implementation of GUI form for choice of visualisations for multiple alignment (both of AA and PB sequences)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'izbor_msa_vizuelizacije.ui'
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
                               QSizePolicy, QVBoxLayout, QWidget, QGroupBox, QHBoxLayout, QRadioButton)

import graphical_reports_alignment_lotos as gl


# class for UI form for choice of visualisations
# contains data about alignment for which visualisation is desired
# FIXME: Names of some functions are on Serbian language
class Ui_Form_MSA_Viz(object):
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

        self.checKBox_Heatmap = QCheckBox(Form)
        self.checKBox_Heatmap.setObjectName(u"checKBox_Heatmap")


        self.verticalLayout.addWidget(self.checKBox_Heatmap)

        self.checkBox_Dendrogram = QCheckBox(Form)
        self.checkBox_Dendrogram.setObjectName(u"checkBox_Dendrogram")

        self.verticalLayout.addWidget(self.checkBox_Dendrogram)

        self.checkBox_Clustering = QCheckBox(Form)
        self.checkBox_Clustering.setObjectName(u"checkBox_Clustering")

        self.verticalLayout.addWidget(self.checkBox_Clustering)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_single = QRadioButton(self.groupBox)
        self.rb_single.setObjectName(u"rb_single")

        self.horizontalLayout.addWidget(self.rb_single)

        self.rb_complete = QRadioButton(self.groupBox)
        self.rb_complete.setObjectName(u"rb_complete")

        self.horizontalLayout.addWidget(self.rb_complete)

        self.rb_avg = QRadioButton(self.groupBox)
        self.rb_avg.setObjectName(u"rb_avg")

        self.horizontalLayout.addWidget(self.rb_avg)

        self.verticalLayout.addWidget(self.groupBox)

        self.pb_Generisi = QPushButton(Form)
        self.pb_Generisi.setObjectName(u"pb_Generisi")

        self.verticalLayout.addWidget(self.pb_Generisi)
        self.pb_Generisi.clicked.connect(self.pbGenerisi_clicked)
        self.checkBox_Clustering.stateChanged.connect(self.change_distance_choice)

        self.labels = None
        self.alignment_data = None

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Izaberi zeljenu vizuelizaciju/vizuelizacije", None))
        self.checkBox_Classic.setText(QCoreApplication.translate("Form", u"Klasicna vizuelizacija poravnanja", None))
        self.checKBox_Heatmap.setText(QCoreApplication.translate("Form", u"Matrica rastojanja prikazana preko heatmap-a", None))
        self.checkBox_Dendrogram.setText(QCoreApplication.translate("Form", u"Drvo spajanja na osnovu matrice rastojanja", None))
        self.checkBox_Clustering.setText(
            QCoreApplication.translate("Form", u"Izgradnja drveta primenom hijerarhijskog klasterovanja", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Choose distance measure", None))
        self.rb_single.setText(QCoreApplication.translate("Form", u"Single distance", None))
        self.rb_single.setChecked(True)
        self.rb_complete.setText(QCoreApplication.translate("Form", u"Complete distance", None))
        self.rb_avg.setText(QCoreApplication.translate("Form", u"Avg distance", None))
        self.rb_avg.setText(QCoreApplication.translate("Form", u"Avg distance", None))
        self.pb_Generisi.setText(QCoreApplication.translate("Form", u"Generisi vizuelizacije", None))
    # retranslateUi

    def pbGenerisi_clicked(self):
        if self.checkBox_Classic.isChecked():
            file_name = 'graphical_report_classic_multi_alignment_visualisation__' + str(datetime.date.today()) + "__" + str(
                datetime.datetime.now().hour) \
                        + "_" + str(datetime.datetime.now().minute) + '.pdf'
            print('Graphical export rendered in file ' + file_name, file=sys.stderr)
            gl.graphical_classic_multi_alignment_visualisation(self.alignment_data, self.labels, file_name)
        if self.checkBox_Dendrogram.isChecked():
            file_name = 'graphical_report_dendrogram__' + str(datetime.date.today()) + "__" + str(
                datetime.datetime.now().hour) \
                        + "_" + str(datetime.datetime.now().minute) + '.pdf'
            print('Graphical export rendered in file ' + file_name, file=sys.stderr)
            gl.graphical_dendrogram_multi_alignment_visualisation(self.alignment_data, self.labels, file_name)
        if self.checKBox_Heatmap.isChecked():
            file_name = 'graphical_report_heatmap__' + str(datetime.date.today()) + "__" + str(
                datetime.datetime.now().hour) \
                        + "_" + str(datetime.datetime.now().minute) + '.pdf'
            print('Graphical export rendered in file ' + file_name, file=sys.stderr)
            gl.graphical_heatmap_multi_alignment_visualisation(self.alignment_data, self.labels, file_name)
        if self.checkBox_Clustering.isChecked():
            if self.rb_single.isChecked():
                file_name = 'graphical_report_clustering_dendrogram_single_linkage__' + str(datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_dendrogram_by_hierarchical_clustering(self.alignment_data, 'single', file_name)
            elif self.rb_avg.isChecked():
                file_name = 'graphical_report_clustering_dendrogram_avg_linkage__' + str(
                    datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_dendrogram_by_hierarchical_clustering(self.alignment_data, 'avg', file_name)
            elif self.rb_complete.isChecked():
                file_name = 'graphical_report_clustering_dendrogram_complete_linkage__' + str(
                    datetime.date.today()) + "__" + str(
                    datetime.datetime.now().hour) \
                            + "_" + str(datetime.datetime.now().minute) + '.pdf'
                print('Graphical export rendered in file ' + file_name, file=sys.stderr)
                gl.graphical_dendrogram_by_hierarchical_clustering(self.alignment_data, 'complete', file_name)

    def ocisti_izbor(self):
        self.checkBox_Classic.setChecked(False)
        self.checkBox_Dendrogram.setChecked(False)
        self.checKBox_Heatmap.setChecked(False)
        self.checkBox_Clustering.setChecked(False)
        self.alignment_data = None
        self.labels = None

    def set_alignment_data(self, alignment_data):
        self.alignment_data = alignment_data

    def set_labels(self, labels):
        self.labels = labels

    def change_distance_choice(self):
        b = self.groupBox.isEnabled()
        self.groupBox.setEnabled(not b)


# class for window whose UI is implemented class above
# FIXME: Names of some functions are on Serbian language
class WidgetMSAVizuelizacija(QWidget):
    def __init__(self):
        super(WidgetMSAVizuelizacija, self).__init__()
        self.ui = Ui_Form_MSA_Viz()
        self.ui.setupUi(self)
        self.setWindowTitle("Izaberi vizuelizacije")

    def ocisti_izbor(self):
        self.ui.ocisti_izbor()

    def set_alignment_data(self, alignment_data):
        self.ui.set_alignment_data(alignment_data)

    def set_labels(self, labels):
        self.ui.set_labels(labels)

