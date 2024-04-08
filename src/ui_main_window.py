# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vlayout = QVBoxLayout()
        self.vlayout.setObjectName(u"vlayout")
        self.vlayout.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.vlayout.addWidget(self.label)

        self.label_edit = QLineEdit(self.centralwidget)
        self.label_edit.setObjectName(u"label_edit")

        self.vlayout.addWidget(self.label_edit)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vlayout.addItem(self.verticalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.vlayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.type_btns = QButtonGroup(MainWindow)
        self.type_btns.setObjectName(u"type_btns")
        self.type_btns.setExclusive(False)
        self.type_btns.addButton(self.checkBox_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 3, 3, 1, 1)

        self.checkBox_15 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_15)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout.addWidget(self.checkBox_15, 0, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_12)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout.addWidget(self.checkBox_12, 5, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_13)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout.addWidget(self.checkBox_13, 3, 4, 1, 1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_8)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout.addWidget(self.checkBox_8, 1, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_16)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout.addWidget(self.checkBox_16, 0, 2, 1, 1)

        self.checkBox_11 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_11)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout.addWidget(self.checkBox_11, 5, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 3, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_7)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 0, 4, 1, 1)

        self.checkBox_14 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_14)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout.addWidget(self.checkBox_14, 1, 2, 1, 1)

        self.checkBox_10 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_10)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 0, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_6)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 0, 3, 1, 1)

        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_9)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 3, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.type_btns.addButton(self.checkBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 6, 0, 1, 1)


        self.vlayout.addLayout(self.gridLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vlayout.addItem(self.verticalSpacer_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.vlayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.sort_combo = QComboBox(self.centralwidget)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sort_combo.sizePolicy().hasHeightForWidth())
        self.sort_combo.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.sort_combo)

        self.radioButton = QRadioButton(self.centralwidget)
        self.sort_btns = QButtonGroup(MainWindow)
        self.sort_btns.setObjectName(u"sort_btns")
        self.sort_btns.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy1.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy1)
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.sort_btns.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy1.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.vlayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vlayout.addItem(self.verticalSpacer_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.vlayout.addWidget(self.label_4)

        self.include_sold_out_btn = QCheckBox(self.centralwidget)
        self.include_sold_out_btn.setObjectName(u"include_sold_out_btn")
        sizePolicy1.setHeightForWidth(self.include_sold_out_btn.sizePolicy().hasHeightForWidth())
        self.include_sold_out_btn.setSizePolicy(sizePolicy1)

        self.vlayout.addWidget(self.include_sold_out_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gen_btn = QPushButton(self.centralwidget)
        self.gen_btn.setObjectName(u"gen_btn")
        sizePolicy1.setHeightForWidth(self.gen_btn.sizePolicy().hasHeightForWidth())
        self.gen_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.gen_btn)


        self.vlayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.vlayout, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Artist/Label Name ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Merch Type", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Hat", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Cassette", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Bag", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Other Apparel", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"T-Shirt/Shirt", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Sheet Music", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"Compact Disc (CD)", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Sweater/Hoodie", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"USB Flash Drive", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Book/Magazine", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Record/Vinyl", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"DVD", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Poster/Print", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"T-Shirt/Apparel", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sort By", None))
        self.sort_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Nothing", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Artist", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Price", None))
        self.sort_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Title", None))
        self.sort_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Type", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Descending", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Other Options", None))
        self.include_sold_out_btn.setText(QCoreApplication.translate("MainWindow", u"Include Sold Out", None))
        self.gen_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

