from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Tkinter import *
import os
import sys
import urllib2


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/dialog.ui'))


class YoutubeDialog(QMainWindow, FORM_CLASS):
    def __init__(self):
        super(YoutubeDialog, self).__init__()
        self.setupUi(self)
        self.window = Tk()
        self.downloadButton.clicked.connect(self.__download)
        self.saveButton.clicked.connect(self.__save)
        self.closeButton.clicked.connect(self.__close)

    def __download(self):
        url = str(self.urlEdit.text())
        if url is not None:
            print("downloading with urllib2")
            req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
            f = urllib2.urlopen(req)
            data = f.read()
            with open("image.jpeg", "wb") as code:
                code.write(data)
        else:
            QMessageBox.warning(self.iface.mainWindow(), self.tr("Nothing to download"), self.tr("There is no Url. So please write the Ulr of your Video that you want to download"))

    def __save(self):
        dateiname = QFileDialog.getExistingDirectory(self, "Save", "/home/hka/Downloads", QFileDialog.ShowDirsOnly)

    def __close(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    form = YoutubeDialog()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
