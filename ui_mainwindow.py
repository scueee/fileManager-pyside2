# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
# from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QSplitter::handle{background-color: rgb(229, 229, 229)}")
        self.openAction = QAction(MainWindow)
        self.openAction.setObjectName(u"openAction")
        self.aboutAction = QAction(MainWindow)
        self.aboutAction.setObjectName(u"aboutAction")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMinimumSize(QSize(20, 20))
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.leftWidget = QWidget(self.splitter)
        self.leftWidget.setObjectName(u"leftWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 0)
        self.tabWidget = QTabWidget(self.leftWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_6 = QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.treeView = QTreeView(self.tab_1)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_6.addWidget(self.treeView)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.splitter.addWidget(self.leftWidget)
        self.rightWidget = QWidget(self.splitter)
        self.rightWidget.setObjectName(u"rightWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth())
        self.rightWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.rightWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 3)
        self.splitter_2 = QSplitter(self.rightWidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.searchWidget = QWidget(self.splitter_2)
        self.searchWidget.setObjectName(u"searchWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.searchWidget.sizePolicy().hasHeightForWidth())
        self.searchWidget.setSizePolicy(sizePolicy4)
        self.gridLayout = QGridLayout(self.searchWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_key = QLabel(self.searchWidget)
        self.label_key.setObjectName(u"label_key")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_key, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.searchWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)

        self.label_fun = QLabel(self.searchWidget)
        self.label_fun.setObjectName(u"label_fun")
        sizePolicy5.setHeightForWidth(self.label_fun.sizePolicy().hasHeightForWidth())
        self.label_fun.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_fun, 0, 0, 1, 1)

        self.searchBtn = QToolButton(self.searchWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.searchBtn, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.radioButton_name = QRadioButton(self.searchWidget)
        self.radioButton_name.setObjectName(u"radioButton_name")
        self.radioButton_name.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_name, 0, 1, 1, 1)

        self.radioButton_full = QRadioButton(self.searchWidget)
        self.radioButton_full.setObjectName(u"radioButton_full")

        self.gridLayout.addWidget(self.radioButton_full, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.splitter_2.addWidget(self.searchWidget)
        self.resultWidget = QWidget(self.splitter_2)
        self.resultWidget.setObjectName(u"resultWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(4)
        sizePolicy7.setHeightForWidth(self.resultWidget.sizePolicy().hasHeightForWidth())
        self.resultWidget.setSizePolicy(sizePolicy7)
        self.verticalLayout_3 = QVBoxLayout(self.resultWidget)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 6, 3, 3)
        self.tableView = QTableView(self.resultWidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.tableView)

        self.splitter_2.addWidget(self.resultWidget)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.splitter.addWidget(self.rightWidget)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.openAction)
        self.menu.addAction(self.aboutAction)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.openAction.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#if QT_CONFIG(tooltip)
        self.openAction.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.aboutAction.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u" \u76ee\u5f55\u7ed3\u6784", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u" \u9884\u89c8\u89c6\u56fe", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5185\u5bb9\uff1a", None))
        self.label_fun.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u65b9\u5f0f\uff1a", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.radioButton_name.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\u68c0\u7d22", None))
        self.radioButton_full.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u68c0\u7d22", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

