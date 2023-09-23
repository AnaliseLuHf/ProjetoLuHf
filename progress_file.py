from qt_core import *
from gui.window.py.ProgressoImportação import *
class LoadingWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ProgressoImportao()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def update_progress(self, progress):
        self.ui.progressBar.setValue(progress)
