# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
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
        self.exitAction = QAction(MainWindow)
        self.exitAction.setObjectName(u"exitAction")
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
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
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
        self.label_fun = QLabel(self.searchWidget)
        self.label_fun.setObjectName(u"label_fun")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_fun.sizePolicy().hasHeightForWidth())
        self.label_fun.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_fun, 0, 0, 1, 1)

        self.checkBox_name = QCheckBox(self.searchWidget)
        self.checkBox_name.setObjectName(u"checkBox_name")

        self.gridLayout.addWidget(self.checkBox_name, 0, 1, 1, 1)

        self.checkBox_full = QCheckBox(self.searchWidget)
        self.checkBox_full.setObjectName(u"checkBox_full")

        self.gridLayout.addWidget(self.checkBox_full, 0, 2, 1, 1)

        self.label_suf = QLabel(self.searchWidget)
        self.label_suf.setObjectName(u"label_suf")
        sizePolicy5.setHeightForWidth(self.label_suf.sizePolicy().hasHeightForWidth())
        self.label_suf.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_suf, 1, 0, 1, 1)

        self.checkBox_pdf = QCheckBox(self.searchWidget)
        self.checkBox_pdf.setObjectName(u"checkBox_pdf")

        self.gridLayout.addWidget(self.checkBox_pdf, 1, 1, 1, 1)

        self.checkBox_doc = QCheckBox(self.searchWidget)
        self.checkBox_doc.setObjectName(u"checkBox_doc")

        self.gridLayout.addWidget(self.checkBox_doc, 1, 2, 1, 1)

        self.checkBox_xls = QCheckBox(self.searchWidget)
        self.checkBox_xls.setObjectName(u"checkBox_xls")

        self.gridLayout.addWidget(self.checkBox_xls, 1, 3, 1, 1)

        self.checkBox_ppt = QCheckBox(self.searchWidget)
        self.checkBox_ppt.setObjectName(u"checkBox_ppt")

        self.gridLayout.addWidget(self.checkBox_ppt, 1, 4, 1, 1)

        self.label_key = QLabel(self.searchWidget)
        self.label_key.setObjectName(u"label_key")
        sizePolicy5.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label_key, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.searchWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 3)

        self.searchBtn = QToolButton(self.searchWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy5.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.searchBtn, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 5, 1, 1)

        self.progressBar = QProgressBar(self.searchWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 5)

        self.splitter_2.addWidget(self.searchWidget)
        self.resultWidget = QWidget(self.splitter_2)
        self.resultWidget.setObjectName(u"resultWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(4)
        sizePolicy6.setHeightForWidth(self.resultWidget.sizePolicy().hasHeightForWidth())
        self.resultWidget.setSizePolicy(sizePolicy6)
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
        self.menu.addAction(self.exitAction)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.openAction.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.exitAction.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u" \u76ee\u5f55\u7ed3\u6784", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u" \u9884\u89c8\u89c6\u56fe", None))
        self.label_fun.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u65b9\u5f0f\uff1a", None))
        self.checkBox_name.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u540d\u79f0", None))
        self.checkBox_full.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u5168\u6587", None))
        self.label_suf.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u683c\u5f0f\uff1a", None))
        self.checkBox_pdf.setText(QCoreApplication.translate("MainWindow", u" *.pdf", None))
        self.checkBox_doc.setText(QCoreApplication.translate("MainWindow", u" *.doc", None))
        self.checkBox_xls.setText(QCoreApplication.translate("MainWindow", u" *.xls", None))
        self.checkBox_ppt.setText(QCoreApplication.translate("MainWindow", u" *.ppt", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5185\u5bb9\uff1a", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi
