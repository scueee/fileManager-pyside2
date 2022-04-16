from PySide2.QtCore import QProcess, Signal, QThread, Qt, QSettings, QRect
from PySide2.QtGui import QFont, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog, QAbstractItemView, QTextEdit, QProgressBar, QMessageBox
import sys
from ui_mainwindow import Ui_MainWindow
from my_worker import Worker

class MainWindow(QMainWindow):
    worker: Worker
    file_path_signal = Signal(str)
    file_search_signal = Signal(bool, str, str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ini = QSettings("config.ini", QSettings.IniFormat)
        # set ui
        self.ui.splitter.setHandleWidth(5)
        self.ui.splitter_2.setHandleWidth(5)
        self.ui.textBrowser.setLineWrapMode(QTextEdit.NoWrap)  # 禁用自动换行
        self.progressBar = QProgressBar()
        self.progressBar.setMaximumHeight(5)
        self.progressBar.setTextVisible(False)
        self.ui.statusbar.addPermanentWidget(self.progressBar)
        # 初始化 treeView
        self.path = self.ini.value("project/path")
        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(self.path))  # 只显示设置的那个文件路径。
        self.ui.treeView.doubleClicked.connect(self.on_treeView_doubleClicked)  # 双击文件打开
        self.ui.treeView.setDragDropMode(QAbstractItemView.InternalMove) # 内部拖拽
        # 初始化 tableView
        self.table_model = QStandardItemModel()
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格只读
        self.ui.tableView.setMouseTracking(True) # 鼠标追踪
        # connect
        self.ui.lineEdit.returnPressed.connect(self.on_searchBtn_clicked)
        self.ui.searchBtn.clicked.connect(self.on_searchBtn_clicked)
        self.ui.openAction.triggered.connect(self.on_openAction_triggered)
        self.ui.aboutAction.triggered.connect(self.on_aboutAction_triggered)
        self.ui.tableView.entered.connect(self.on_tableView_entered)  # show toolTip
        self.ui.tableView.clicked.connect(self.on_tableView_clicked)  # cickToPreview
        self.ui.tableView.doubleClicked.connect(self.on_tableView_doubleClicked)  # doubleCickToOpenFileOrPath
        # 子线程 connect
        self.thread = QThread(self)
        self.thread.start()
        self.worker = Worker() # to get file text or search
        self.worker.moveToThread(self.thread)
        self.file_search_signal.connect(self.worker.fileSearch)
        self.file_path_signal.connect(self.worker.postText)
        self.worker.table_view_signal.connect(self.updateTableView)
        self.worker.file_preview_signal.connect(self.updateTextBrowser)
        self.worker.progress_bar_signal.connect(self.updateProgressBar)

    def on_openAction_triggered(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_1)
        self.path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.ui.treeView.setRootIndex(self.model.index(self.path))
        self.ini.setValue("project/path",self.path)

    def on_aboutAction_triggered(self):
        self.aboutMsg = QMessageBox()
        self.aboutMsg.setWindowTitle("关于")
        self.aboutMsg.setText("author:twj\nversion:1.1\nsupport regex like: .*(pdf|PDF){1}$")
        self.aboutMsg.show()

    def on_treeView_doubleClicked(self, Qmodelidx):
        QProcess.execute("explorer " + self.model.filePath(Qmodelidx).replace("/", "\\"))

    def on_searchBtn_clicked(self):
        self.table_model.clear()
        self.file_search_signal.emit(self.ui.radioButton_name.isChecked(), self.path, self.ui.lineEdit.text())
        # model前面clear了，view的属性设置也会重置
        # self.ui.tableView.setColumnWidth(0,250)
        # self.ui.tableView.setColumnWidth(1,150)
        # self.ui.tableView.resizeColumnsToContents()
        self.table_model.setHorizontalHeaderItem(0, QStandardItem("文件名称"))
        self.table_model.setHorizontalHeaderItem(1, QStandardItem("文件路径"))

    def on_tableView_entered(self, Qmodelidx):
        self.ui.tableView.setToolTip(self.table_model.itemData(Qmodelidx)[0])

    def on_tableView_doubleClicked(self, Qmodelidx):
        row = self.table_model.itemFromIndex(Qmodelidx).row()
        column = self.table_model.itemFromIndex(Qmodelidx).column()
        if column==0:
            ex = f"explorer {self.table_model.data(self.table_model.index(row,1))}"
        else:
            path = self.table_model.itemData(Qmodelidx)[0]
            name = self.table_model.data(self.table_model.index(row,0))
            ex = f"explorer {path[0:len(path)-len(name)]}"
        QProcess.execute(ex.replace("/", "\\"))

    def on_tableView_clicked(self, Qmodelidx):
        self.ui.textBrowser.clear()
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_2)
        self.progressBar.setValue(0)
        # path = self.table_model.itemData(Qmodelidx)[0]
        row = self.table_model.itemFromIndex(Qmodelidx).row()
        path = self.table_model.data(self.table_model.index(row,1))
        self.file_path_signal.emit(path)

    def updateTextBrowser(self, text):
        self.ui.textBrowser.insertPlainText(text)

    def updateProgressBar(self, max, value):
        self.progressBar.setMaximum(max)
        self.progressBar.setValue(value)

    def updateTableView(self, row, item1, item2):
        self.table_model.setItem(row, 0, QStandardItem(item1))
        self.table_model.setItem(row, 1, QStandardItem(item2))

    # 重写 closeEvent
    def closeEvent(self, event):
        self.ini.setValue("winInfo/x",window.geometry().x())
        self.ini.setValue("winInfo/y",window.geometry().y())
        self.ini.setValue("winInfo/w",window.geometry().width())
        self.ini.setValue("winInfo/h",window.geometry().height())
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ini = QSettings("config.ini", QSettings.IniFormat)
    app.setFont(QFont("宋体", int(ini.value("font/size"))))
    window = MainWindow()
    x = int(ini.value("winInfo/x"))
    y = int(ini.value("winInfo/y"))
    w = int(ini.value("winInfo/w"))
    h = int(ini.value("winInfo/h"))
    window.setGeometry(QRect(x,y,w,h))
    window.show()
    sys.exit(app.exec_())

