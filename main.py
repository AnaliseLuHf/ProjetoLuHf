import sys
import os
#import platform
from qt_core import *
from gui.window.py.MainWindow import *
from app.gerenciar_arquivos import * # Classe que gerencia a criação de pastas e arquivos do projeto
from app.dialogs import * # Classe que gerencia as caixas de mensagem que aparecem
from  app.janela_novo_projeto import * # Classe que gerencia a janela para criar um projeto
from app.filtrar_dados import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # Atributos gerais da classe
        self.local_projeto_criado = None
        self.nome_projeto_criado = None
        self.arquivos_selecionados = None


        # Setup a Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Definindo um título para a janela
        self.setWindowTitle("LuHf")

        # Definindo um ícone
        self.setWindowIcon(QIcon("gui/images/icon.png"))

        # Exibindo a janela
        self.show()

        # Conectando o btn_menu a função que irá expandir/retrair o menu quando ele for clicado
        self.ui.btn_menu.clicked.connect(self.expandir_menu)

        # Conectando os botões do menu com as suas  funções
        self.ui.btn_inicio.clicked.connect(self.clique_botao)

        # Botões com as funcionalidades do programa
        self.ui.btn_pagina_novo_projeto.clicked.connect(self.clique_botao)
        self.ui.btn_add_arquivos.clicked.connect(self.clique_botao)
        self.ui.btn_pagina_visualizar_dados_arquivos.clicked.connect(self.clique_botao)


        # Botões que redimensionam a janela
        self.ui.btn_minimizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_maximizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_fechar_janela.clicked.connect(self.clique_botao)


        # Botão para criar um projeto a partir da tela principal
        self.ui.btn_novo_projeto_home.clicked.connect(self.clique_botao)


    # Função que irá expandir e retrair o menu esquerdo
    def expandir_menu(self):
        # Pegando a largura do menu esquerdo
        largura_menu_esquerdo = self.ui.leftMenuContent.width()

        largura_padrao = 60

        if largura_menu_esquerdo == 60:
            largura_padrao = 160

        # Animando a transição
        self.animation = QPropertyAnimation(self.ui.leftMenuContent, b"minimumWidth")
        self.animation.setDuration(900)
        self.animation.setStartValue(largura_menu_esquerdo)
        self.animation.setEndValue(largura_padrao)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()


    # Essa função pega o nome do botão que foi clicado e conecta a uma "função" para ele
    def clique_botao(self):
        # Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        # Pegando o nome do botão que foi clicado
        nome_botao = btn.objectName()

        # Mostra a página inicial da aplicação
        if nome_botao == "btn_inicio":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_inicial)

        # Mostra a janela para criar  projeto
        if nome_botao == "btn_pagina_novo_projeto" or nome_botao == "btn_novo_projeto_home":
            # Abre a janela para criar um projeto
            self.jn_novo_projeto = JanelaNovoProjeto()

            # Muda os atributos da classe principal, pois a janela do novo projeto pega o
            # nome e o local do projeto escolhido pelo usuário
            self.jn_novo_projeto.local_e_nome_projeto.connect(self.mudar_atributos_classe)

            self.jn_novo_projeto.show()


        # Mostra a página para ver os arquivos carregados, já com os dados corrigidos do background
        if nome_botao == "btn_pagina_visualizar_dados_arquivos":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_add_arquivos)

        # Abre a caixa de diálogos para selecionar os arquivos
        if nome_botao == "btn_add_arquivos":
            self.selecionar_arquivos()

        # Minimiza a janela da aplicação
        if nome_botao == "btn_minimizar_janela":
            self.showMinimized()

        # Maximiza a janela da aplicação
        if nome_botao == "btn_maximizar_janela":
            self.showMaximized()

        # Fecha a aplicação
        if nome_botao == "btn_fechar_janela":
            self.close()

    def mudar_atributos_classe(self, valor_local_projeto, valor_nome_projeto):
        self.local_projeto_criado = valor_local_projeto
        self.nome_projeto_criado = valor_nome_projeto


    def verificar_projeto_criado(self):
        if self.local_projeto_criado != None and self.nome_projeto_criado != None:
            return True
        else:
            return False

    def selecionar_arquivos(self):

        status_projeto = self.verificar_projeto_criado()

        if status_projeto == True:
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)

            # Mostra apenas os arquivos com extensão ".exp"
            file_dialog.setNameFilter("Arquivos de Texto (*.exp);")

            if file_dialog.exec():
                # Muda o atributo da classe, com uma lista para os arquivos selecionados
                arquivos_selecionados = file_dialog.selectedFiles()

            # Copiando os arquivos selecionados para a pasta "data" do projeto
            caminho_pasta_data = self.local_projeto_criado + "/" + self.nome_projeto_criado + "/data"

            try:
                GerenciarArquivos.copiar_arquivos(self, arquivos_selecionados, caminho_pasta_data)

                # Pegando o caminho dos arquivos copiados para a pasta data, para passar como uma lista
                # sendo um atributo da classe
                caminhos_arquivos_data = []

                for arquivo in os.listdir(caminho_pasta_data):
                    caminho_arquivo = caminho_pasta_data + "/" + arquivo
                    if os.path.isfile(caminho_arquivo):
                        caminhos_arquivos_data.append(caminho_arquivo)

                # Mudando o atributo da classe, para uma lista com o nome dos arquivos selecionados
                self.arquivos_selecionados = caminhos_arquivos_data

                # Chamando a função que irá filtar os dados originais, eliminando os dados desnecessários
                FiltarDadosArquivosOriginais.excluir_dados_desnecessarios(self, self.arquivos_selecionados)



            except Exception as e:
                DialogosSistema.msg_usuario(self, str(e), tipo = "Erro")

        else:
            DialogosSistema.msg_alerta_crie_projeto(self,"Crie um projeto antes de importar os arquivos!")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
