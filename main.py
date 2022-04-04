from PySide2.QtCore import QProcess, QDirIterator, Signal, QThread
from PySide2.QtGui import QFont, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog, QAbstractItemView, QTextEdit
import sys
import re
from ui_mainwindow import Ui_MainWindow
from my_worker import Worker

class MainWindow(QMainWindow):
    worker: Worker
    file_path_signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # set ui
        self.ui.splitter.setHandleWidth(5)
        self.ui.splitter_2.setHandleWidth(5)
        self.ui.textBrowser.setLineWrapMode(QTextEdit.NoWrap)  # 禁用自动换行
        # 初始化 tableView
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderItem(0, QStandardItem("文件名称"))
        self.table_model.setHorizontalHeaderItem(1, QStandardItem("文件路径"))
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格只读
        self.ui.tableView.setMouseTracking(True) # 鼠标追踪
        # connect
        self.ui.searchBtn.clicked.connect(self.on_searchBtn_clicked)
        self.ui.openAction.triggered.connect(self.on_openAction_triggered)
        self.ui.exitAction.triggered.connect(self.on_exitAction_triggered)
        self.ui.tableView.entered.connect(self.on_tableView_entered)  # show toolTip
        self.ui.tableView.clicked.connect(self.on_tableView_clicked)  # clickToPreview
        self.thread = QThread(self)
        self.thread.start()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.file_path_signal.connect(self.worker.postText)
        self.worker.file_preview_signal.connect(self.updateTextBrowser)
        self.worker.progress_bar_signal.connect(self.updateProgressBar)

    def on_openAction_triggered(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_1)
        self.path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(self.path))  # 只显示设置的那个文件路径。
        self.ui.treeView.doubleClicked.connect(self.on_treeView_doubleClicked)  # 双击文件打开

    def on_treeView_doubleClicked(self, Qmodelidx):
        QProcess.execute("explorer " + self.model.filePath(Qmodelidx).replace("/", "\\"))

    def on_searchBtn_clicked(self):
        # 查找并写入
        if self.ui.checkBox_name.isChecked():
            p_suf = ".*"
            if self.ui.checkBox_pdf.isChecked():
                p_suf = p_suf + r"(pdf|PDF){1}$"
            if self.ui.checkBox_doc.isChecked():
                if "$" in p_suf:
                    p_suf = p_suf[0:-5] + r"|doc|docx){1}$"
                else:
                    p_suf = p_suf + r"(doc|docx){1}$"
            if self.ui.checkBox_xls.isChecked():
                if "$" in p_suf:
                    p_suf = p_suf[0:-5] + r"|xls|xlsx){1}$"
                else:
                    p_suf = p_suf + r"(xls|xlsx){1}$"
            if self.ui.checkBox_ppt.isChecked():
                if "$" in p_suf:
                    p_suf = p_suf[0:-5] + r"|ppt|pptx){1}$"
                else:
                    p_suf = p_suf + r"(ppt|pptx){1}$"
            p_c = re.compile(self.ui.lineEdit.text() + p_suf)
            dirIt = QDirIterator(self.path, QDirIterator.Subdirectories)  # 获取目录信息
            i = 0
            self.table_model.clear()
            while dirIt.hasNext():
                dirIt.next()
                if re.search(p_c, dirIt.fileName()):
                    # 写入 tableView
                    self.table_model.setItem(i, 0, QStandardItem(dirIt.fileName()))
                    self.table_model.setItem(i, 1, QStandardItem(dirIt.filePath()))
                    i += 1
        # model一旦变化，view的列宽设置也会重置
        self.ui.tableView.setColumnWidth(0,250)
        self.ui.tableView.setColumnWidth(1,150)
        # self.ui.tableView.resizeColumnsToContents()

    def on_exitAction_triggered(self):
        sys.exit(self)

    def on_tableView_entered(self, Qmodelidx):
        self.ui.tableView.setToolTip(self.table_model.itemData(Qmodelidx)[0])

    def on_tableView_clicked(self, Qmodelidx):
        self.ui.textBrowser.clear()
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_2)
        self.ui.progressBar.setValue(0)
        # path = self.table_model.itemData(Qmodelidx)[0]
        row = self.table_model.itemFromIndex(Qmodelidx).row()
        path = self.table_model.data(self.table_model.index(row,1))
        self.file_path_signal.emit(path)

    def updateTextBrowser(self, text):
        self.ui.textBrowser.insertPlainText(text)

    def updateProgressBar(self, max, value):
        self.ui.progressBar.setMaximum(max)
        self.ui.progressBar.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("宋体", 12))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

