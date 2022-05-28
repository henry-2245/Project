# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderhistory.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
import search

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #DAE5D0;\n"
"}")
        self.history_order = QLabel(Dialog)
        self.history_order.setObjectName(u"history_order")
        self.history_order.setGeometry(QRect(80, 40, 211, 51))
        self.history_order.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	font: 24pt \"MS Shell Dlg 2\";\n"
"	background-color: #C2DED1;\n"
"	border: 2px solid #14C38E;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"")
        self.orderBackButton = QPushButton(Dialog)
        self.orderBackButton.setObjectName(u"orderBackButton")
        self.orderBackButton.setGeometry(QRect(10, 10, 41, 41))
        font = QFont()
        font.setPointSize(16)
        self.orderBackButton.setFont(font)
        self.orderBackButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/searchicon/icons8-left-arrow-26.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(111, 218, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid black;\n"
"	background-color: rgb(140, 238, 179)\n"
"}")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 120, 351, 591))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: #DAE5D0;\n"
"	border: 6px inset #14C38E;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	background-color: #DAE5D0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(57, 68, 84);\n"
"    color: white;\n"
"	border: 1px solid rgb(111, 218, 156);\n"
"}\n"
"\n"
"QHeaderView::section:hover{\n"
"	border: 1px solid green;\n"
"	background-color: rgb(80, 110, 125);\n"
"}\n"
"\n"
"QHeaderView::section:first{\n"
"	border-top-left-radius:5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:last{\n"
"	border-bottom-right-radius: 5px;\n"
"}")
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(113)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.history_order.setText(QCoreApplication.translate("Dialog", u"Order History", None))
        self.orderBackButton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Shop", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Item", None));
    # retranslateUi

