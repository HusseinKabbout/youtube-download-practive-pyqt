from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import sys
import pytube
import resources

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/dialog.ui'))


FORM_RES_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/resolution.ui'))


class YoutubeDialog(QDialog, FORM_CLASS):

    def __init__(self):
        super(YoutubeDialog, self).__init__()

        self.setupUi(self)
        self.downloadButton.clicked.connect(self.__download)
        self.saveButton.clicked.connect(self.__save)
        self.closeButton.clicked.connect(self.__close)

    def __download(self):

        url = self.urlEdit.text()
        # TODO: add url validator
        if url and url is "":
            QMessageBox.warning(self,
                                "URL Error",
                                "Please provide a valid URL")
            return

        if self.saveEdit.text() and self.saveEdit.text() is "":
            QMessageBox.warning(self,
                                "Save path Error",
                                "Please provide a path")
            return
        # TODO: find better library
        yt = pytube.YouTube(url)
        videos = yt.get_videos()

        vid = videos[2]

        vid.download(self.saveEdit.text())

        QMessageBox.success(self,
                            "Success",
                            yt.filename + "\nHas been successfully downloaded")
        # TODO: add progressBar

    def __save(self):
        # Fix me
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
