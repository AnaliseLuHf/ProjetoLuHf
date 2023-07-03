import sys
import os
import platform
from qt_core import *
from gui.window.py.main_window import *
from app.gerenciar_arquivos import * # Classe que gerencia a criação de pastas e arquivos do projeto
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Passa o caminho onde esta a pasta do projeto como um atributo. Assim, esse caminho pode ser usado por vários métodos.
        self.local_projeto = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Por padrão, o local será User>Desktop

        #Atributo para o nome do projeto, para que ele possa ser usado por outro métodos
        self.nome_projeto = "LuHf" + str(datetime.now()) #Por padrão, sera LuHF + Data e Hore quando foi criado

        '''#Este método retira a barra superior padrão do Windows
        self.setWindowFlags(Qt.FramelessWindowHint)'''
        # Setup a Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Exibindo a janela
        self.show()

        # Conectando o btn_menu a função que irá expandir/retrair o menu quando ele for clicado
        self.ui.btn_menu.clicked.connect(self.expandir_menu)

        # Conectando os botões do menu com as suas  funções
        self.ui.btn_inicio.clicked.connect(self.clique_botao)
        self.ui.btn_novo_projeto.clicked.connect(self.clique_botao)
        self.ui.btn_minimizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_maximizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_fechar_janela.clicked.connect(self.clique_botao)

        #Conectando o botão btn_selecionar_local_projeto com a função para selecionar o local onde a pasta do projeto ficará salva
        self.ui.btn_selecionar_local_projeto.clicked.connect(self.selecionar_local_projeto)

        #Conectando o botão btn_criar_projeto a função que irá criar uma pasta para o projeto
        self.ui.btn_criar_projeto.clicked.connect(self.criar_novo_projeto)




    # Função que irá expandir e retrair o menu esquerdo
    def expandir_menu(self):
        # Pegando a largura do menu esquerdo
        largura_menu_esquerdo = self.ui.leftMenuContent.width()

        largura_padrao = 60

        if largura_menu_esquerdo == 60:
            largura_padrao = 200

        #Animando a transição
        self.animation = QPropertyAnimation(self.ui.leftMenuContent, b"minimumWidth")
        self.animation.setDuration(900)
        self.animation.setStartValue(largura_menu_esquerdo)
        self.animation.setEndValue(largura_padrao)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

    #Essa função pega o nome do botão que foi clicado e conecta a uma "função" para ele
    def clique_botao(self):
        #Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        #Pegano o nome do botão que foi clicado
        nome_botao = btn.objectName()

        #Mostra a página inicial da aplicação
        if nome_botao == "btn_inicio":
            self.ui.stackedWidget.setCurrentIndex(0)

        #Mostra a pagina para criar um novo projeto
        if nome_botao == "btn_novo_projeto":
            self.ui.stackedWidget.setCurrentIndex(1)

        #Minimiza a janela da aplicação
        if nome_botao == "btn_minimizar_janela":
            self.showMinimized()


        #Maximiza a janela da aplicação
        if nome_botao == "btn_maximizar_janela":
            self.showMaximized()

        #Fecha a aplicação
        if nome_botao == "btn_fechar_janela":
            self.close()


    def selecionar_local_projeto(self):
        dialog = QFileDialog()
        #Define para que seja escolhida apenas pastas
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec():
            #Pega o  caminho_local_projeto da pasta que foi selecionada
            self.local_projeto = dialog.selectedFiles()[0]

        self.ui.label_local_projeto.setText(self.local_projeto)

    def criar_novo_projeto(self):
        self.nome_projeto = self.ui.lineEdit_nome_projeto.text()
        self.local_projeto = self.ui.label_local_projeto.text()

        #Verificando se o nome do projeto e o local onde ficará salvo estão vazios
        if not self.nome_projeto.strip():
            #Se self.nome_projeto estiver vazio o nome padrão será LuHf + Data e Hora de criação
            #O nome precisa ser corrigido pois ele possui caracteres invalidos para os nomes das pastas (: e .)
            nome_corrigido = "LuHf-"+ str(datetime.now()).replace(':', '-').replace('.', '_')
            self.nome_projeto = nome_corrigido

        if not self.local_projeto.strip():
            #Se self.local_projeto estiver vazio o local padrão sera a pasta User>Desktop do PC
            self.local_projeto= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        #Chamando o método da clase GerenciarArquivos, para criar a pasta com o nome e local desejado
        GerenciarArquivos.criar_pasta(self,local=self.local_projeto, nome_pasta=self.nome_projeto)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
