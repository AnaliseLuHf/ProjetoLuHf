from gui.window.py.DialogoExito import *
from gui.window.py.DialogoErro import *
from gui.window.py.DialogoInfo import *
from qt_core import *


class DialogoExito(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogExito()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Passando a mensagem para a janela
        self.ui.label_mensagem.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_fechar.clicked.connect(self.fechar_janela)
        self.ui.btn_ok.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class DialogoErro(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogErro()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Passando a mensagem para a janela
        self.ui.label_mensagem.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_fechar.clicked.connect(self.fechar_janela)
        self.ui.btn_ok.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

class DialogoInfo(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogInfo()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Passando a mensagem para a janela
        self.ui.label_mensagem.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_fechar.clicked.connect(self.fechar_janela)
        self.ui.btn_ok.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()








