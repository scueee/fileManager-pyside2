from PySide2.QtCore import Signal, QObject, Slot
import re
import pdfplumber
import win32com.client  # pypiwin32

class Worker(QObject):
    file_preview_signal = Signal(str)
    progress_bar_signal = Signal(int, int)

    @Slot(str)
    def postText(self, path: str):
        if re.search(".*(pdf|PDF){1}$", path):
            self.postPdfText(path)
        elif re.search(".*(doc|docx){1}$", path):
            self.postWordText(path)
        elif re.search(".*(xls|xlsx){1}$", path):
            self.postExcelText(path)
        elif re.search(".*(ppt|pptx){1}$", path):
            self.postPptText(path)
        else:
            pass

    def postPdfText(self, path: str):
        with pdfplumber.open(path) as pdf:
            progMax = len(pdf.pages)
            for page in pdf.pages:
                text = page.extract_text()
                progValue = page.page_number
                self.file_preview_signal.emit(text)
                self.progress_bar_signal.emit(progMax, progValue)

    def postWordText(self, path: str):
        self.app = win32com.client.DispatchEx('Word.Application')  # 打开独立进程word应用程序
        self.app.Visible = 0  # 后台运行,不显示
        self.app.DisplayAlerts = 0  # 不警告
        # doc = self.app.Documents.Open(FileName=path, Encoding='gbk')
        doc = self.app.Documents.Open(path)
        progMax = len(doc.paragraphs) - 1
        for idx, item in enumerate(doc.paragraphs):
            self.progress_bar_signal.emit(progMax, idx)
            self.file_preview_signal.emit(item.Range.Text)
        # for t in doc.Tables:
        #     for row in t.Rows:
        #         for cell in row.Cells:
        #             print(cell.Range.Text)
        self.app.Documents.Close(SaveChanges=0)
        self.app.Quit()

    def postExcelText(self, path: str):
        self.app = win32com.client.DispatchEx('Excel.Application')  # 打开独立进程
        self.app.Visible = 0  # 后台运行,不显示
        self.app.DisplayAlerts = 0  # 不警告
        xls = self.app.Workbooks.Open(path)
        row = xls.Worksheets(1).UsedRange.Rows.Count
        value_1 = xls.Worksheets(1).UsedRange.Value
        block_size = 10
        n = int(row / block_size)
        n2 = int(row % block_size)
        if n > 0:
            for i in range(n):
                self.progress_bar_signal.emit(row, i)
                text = ""
                for j in range(block_size):
                    int_tmp = i * block_size + j
                    str_tmp = " | ".join(map(lambda x: str(x), value_1[int_tmp]))
                    text = f"{text}{str_tmp}\n"
                self.file_preview_signal.emit(text)
        self.progress_bar_signal.emit(row, row)
        text = ""
        for j in range(n2):
            text = text + " | ".join(map(lambda x: str(x), value_1[row-n2-j])) + "\n"
        self.file_preview_signal.emit(text)
        xls.Close()
        self.app.Documents.Close(SaveChanges=0)
        self.app.Quit()

    def postPptText(self, path: str):
        self.app = win32com.client.DispatchEx('PowerPoint.Application')  # 打开独立进程应用
        self.app.Visible = 0  # 后台运行,不显示
        self.app.DisplayAlerts = 0  # 不警告
        ppt = self.app.Presentations.Open(path)
        page_count = ppt.Slides.Count
        for i in range(1,page_count+1):
            shape_count = ppt.Slides(i).Shapes.Count
            text = ""
            for j in range(1,shape_count+1):
                if ppt.Slides(i).Shapes(j).HasTextFrame:
                    text += ppt.Slides(i).Shapes(j).TextFrame.TextRange.Text
            self.file_preview_signal.emit(text)
            self.progress_bar_signal.emit(page_count, i)
        self.app.Documents.Close(SaveChanges=0)
        self.app.Quit()
