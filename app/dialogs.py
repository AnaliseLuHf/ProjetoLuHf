from gui.window.py.DialogoExito import *
from gui.window.py.DialogoErro import *
from gui.window.py.DialogoInfo import *
from gui.window.py.DialogoInterativa import *
from qt_core import *


class DialogoExito(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogExito()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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

class DialogoInterativo(QDialog):
    opcaoSelecionada = Signal(str)
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogInterativa()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Passando a mensagem para a janela
        self.ui.label_mensagem.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_fechar.clicked.connect(self.close)
        self.ui.btn_sim.clicked.connect(self.enviar_sinal)
        self.ui.btn_nao.clicked.connect(self.close)

    def enviar_sinal(self):
        # Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        # Pegando o nome do botão que foi clicado
        nome_botao = btn.objectName()

        if nome_botao == "btn_sim":
            self.opcaoSelecionada.emit("Sim")
            self.accept()
            self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()






