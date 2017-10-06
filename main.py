from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui.ui_resolution import Ui_dialog
import os
import sys
import pytube
import resources
import validators

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/dialog.ui'))


class YoutubeDialog(QMainWindow, FORM_CLASS):
    def __init__(self):
        super(YoutubeDialog, self).__init__()
        self.setupUi(self)
        self.downloadButton.clicked.connect(self.__download)
        self.saveButton.clicked.connect(self.__save)
        self.closeButton.clicked.connect(self.__close)

    def __download(self):
        Url = str(self.urlEdit.text())
        if validators.url(Url):
            self.completed = 0
            dialog = QDialog()
            dialog.ui = Ui_dialog()
            dialog.ui.setupUi(dialog)

            yt = pytube.YouTube(Url)
            videos = yt.get_videos()

            s = 1
            for v in videos:
                i = str(s) + ". " + str(v)
                dialog.ui.resoList.addItem(i)
                s += 1

            dialog.exec_()
            vid = videos[2]
            text = self.saveEdit.text()
            vid.download(text)
            print(yt.filename + "\nHas been successfully downloaded")
            goDo = self.progressBar.value()
            while goDo < 100:
                self.completed += 0.0001
                self.progressBar.setValue(self.completed)
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error 404")
            msgBox.setText("There is no Url.\n"
                           "Please write the Ulr of your Video that"
                           "you want to download")
            msgBox.addButton(QPushButton("exit"), QMessageBox.RejectRole)
            msgBox.exec_()

    def __save(self):
        dateiname = QFileDialog.getExistingDirectory(
            self, "Save", "/home/hka/", QFileDialog.ShowDirsOnly)
        self.saveEdit.setText(dateiname)

    def __close(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    form = YoutubeDialog()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
