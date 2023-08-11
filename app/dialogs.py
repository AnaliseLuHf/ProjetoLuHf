# Esta classe irá gerenciar as caixas de mensagem que irão aparecer no app
from qt_core import *
from gui.window.py.NovoProjeto import *


class DialogosSistema(QDialog):

    def __init__(self):
        super().__init__()


    def msg_usuario(self, mensagem, tipo):
        dialog_janela_msg = QMessageBox()
        dialog_janela_msg.setWindowTitle("Alerta!")
        dialog_janela_msg.setFixedWidth(300)
        dialog_janela_msg.setText(mensagem)

        # Definir um ícone personalizado
        # Definir uma nova imagem usando QPixmap
        if tipo == "Exito":
            arquivo_img = 'exito40.png'

        if tipo == "Erro":
            arquivo_img = 'erro40.png'

        pixmap = QPixmap(f'C:/Users/arjun/Projetos/ProjetoLuHf/gui/images/icones_dialogs/{arquivo_img}')
        dialog_janela_msg.setIconPixmap(pixmap)

        dialog_janela_msg.exec()

    # Essa função vai exibir uma mensagem caso o usuário tente adicionar arquivos ao programa, sem antes ter criado uma pasta para isso
    def msg_alerta_crie_projeto(self, mensagem):
        dialog_msg_alerta_crie_projeto = QMessageBox()
        dialog_msg_alerta_crie_projeto.setWindowTitle("Crie um projeto!")
        dialog_msg_alerta_crie_projeto.setFixedWidth(300)
        dialog_msg_alerta_crie_projeto.setText(mensagem)
        pixmap = QPixmap(f'C:/Users/arjun/Projetos/ProjetoLuHf/gui/images/icones_dialogs/info40.png')
        dialog_msg_alerta_crie_projeto.setIconPixmap(pixmap)
        dialog_msg_alerta_crie_projeto.exec()




