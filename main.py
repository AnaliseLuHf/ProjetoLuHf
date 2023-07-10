import sys
import os
#import platform
from qt_core import *
from gui.window.py.main_window import *
from app.gerenciar_arquivos import * # Classe que gerencia a criação de pastas e arquivos do projeto
from app.dialogs import * # Classe que gerencia as caixas de mensagem que aparecem
from datetime import datetime # Usado para gerar um nome aleatório para  o projeto, caso seja necessário



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Passa o caminho onde esta a pasta do projeto como um atributo. Assim, esse caminho pode ser usado por vários métodos.
        self.local_projeto = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Por padrão, o local será User>Desktop

        # Atributo para o nome do projeto, para que ele possa ser usado por outro métodos
        self.nome_projeto = "LuHf" + str(datetime.now()) #Por padrão, sera LuHF + Data e Hore quando foi criado

        ''''#Este método retira a barra superior padrão do Windows
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

        # Botões com as funcionalidade do programa
        self.ui.btn_pagina_novo_projeto.clicked.connect(self.clique_botao)
        self.ui.btn_pagina_add_arquivos.clicked.connect(self.clique_botao)
        self.ui.btn_add_arquivos_dados.clicked.connect(self.clique_botao)

        # Botões que redimensionam a janela
        self.ui.btn_minimizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_maximizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_fechar_janela.clicked.connect(self.clique_botao)

        # Conectando o botão btn_selecionar_local_projeto com a função para selecionar o local onde a pasta do projeto ficará salva
        self.ui.btn_selecionar_local_projeto.clicked.connect(self.selecionar_local_projeto)

        # Conectando o botão btn_criar_projeto a função que irá criar uma pasta para o projeto
        self.ui.btn_criar_projeto.clicked.connect(self.criar_novo_projeto)



    # Função que irá expandir e retrair o menu esquerdo
    def expandir_menu(self):
        # Pegando a largura do menu esquerdo
        largura_menu_esquerdo = self.ui.leftMenuContent.width()

        largura_padrao = 60

        if largura_menu_esquerdo == 60:
            largura_padrao = 200

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

        # Mostra a pagina para criar um novo projeto
        if nome_botao == "btn_pagina_novo_projeto":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_novo_projeto)

        # Mostra a página para ver os arquivos carregados, já com os dados corrigidos do background
        if nome_botao == "btn_pagina_add_arquivos":
            # Verifica se existe um projeto criando antes de adicionar os arquivos
            status_projeto = self.verificar_existencia_projeto()

            # Se o projeto não tiver sido criado, o programa muda para a página onde se cria um novo projeto
            if status_projeto == False:
                self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_novo_projeto)

            # Se o projeto tiver sido criado, o programa muda para a página onde é possível selecionar os arquivos com os dados
            else:
                self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_add_arquivos)


        if nome_botao == "btn_add_arquivos_dados":
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

    # Função que seleciona o local onde o projeto ficará salvo
    def selecionar_local_projeto(self):
        dialog = QFileDialog()
        # Define para que seja escolhida apenas pastas
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec():
            # Pega o  caminho  da pasta que foi selecionada
            self.local_projeto = dialog.selectedFiles()[0]

        # Mostra o local selecionado no no campo label_local_projeto
        self.ui.label_local_projeto.setText(self.local_projeto)

    # Função que cria uma novo projeto
    def criar_novo_projeto(self):
        try:
            self.nome_projeto = self.ui.lineEdit_nome_projeto.text()
            self.local_projeto = self.ui.label_local_projeto.text()

            # Verificando se o local onde é inserido o nome do projeto e o local onde ficará salvo estão vazios
            if not self.nome_projeto.strip():
                # Se self.nome_projeto estiver vazio o nome padrão será Analise Lu e Hf + Data e Hora de criação
                nome_corrigido = "Análise Lu e Hf-" + str(datetime.now()).replace(':', '-').replace('.', '_')  # O nome precisa ser corrigido pois ele possui caracteres invalidos para os nomes das pastas (: e .)
                self.nome_projeto = nome_corrigido

            if not self.local_projeto.strip():
                # Se self.local_projeto estiver vazio o local padrão sera a pasta User>Desktop do PC
                self.local_projeto = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

            # Chamando o método da clase GerenciarArquivos, para criar a pasta com o nome e local desejado
            GerenciarArquivos.criar_pasta(self, local=self.local_projeto, nome_pasta=self.nome_projeto)

            # Se a criação da pasta do projeto teve exito
            mensagem = "Projeto criado com sucesso!"

            # Mostrando uma mensagem informando que o projeto foi criado
            DialogosSistema.msg_criacao_projeto(self, mensagem, tipo="Exito")

        # Se tiver algum erro durante a criação da pasta
        # Caso o local selecionado para salvar o projeto já tenha uma pasta como o nome escolhido
        except FileExistsError:
            mensagem = f"'{self.nome_projeto}' já existe em '{self.local_projeto}'"
            DialogosSistema.msg_criacao_projeto(self, mensagem, tipo="Erro")

        # Caso o usuário não possua acesso ao local selecionado para salvar o projeto
        except PermissionError:
            mensagem = f"Acesso restrito a '{self.local_projeto}'!"
            DialogosSistema.msg_criacao_projeto(self, mensagem, tipo="Erro")

        # Ou qualquer outro erro que apareça
        except:
            mensagem = "Erro!"
            DialogosSistema.msg_criacao_projeto(self, mensagem, tipo="Erro")

        # Após o projeto ter sido criado, o programa vai automaticamente para a pasta para selecionar os arquivos com os dados
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_add_arquivos)

        # Mostra o nome do projeto no header do programa
        self.ui.label_nome_projeto.setText(f"{self.nome_projeto}")

    # Esta função irá verificar se o projeto foi criado (se existe uma pasta para ele), pois todas as funcionalidades do programa dependem disso
    def verificar_existencia_projeto(self):
        caminho_projeto = self.local_projeto + "/"+ self.nome_projeto
        # Verifica se o projeto existe ou não
        status_projeto = GerenciarArquivos.verificar_pasta(self, caminho_projeto)
        if status_projeto == False:
            # Mostra uma mensagem informando para criar um projeto antes de adicionar os arquivos
            DialogosSistema.msg_alerta_crie_projeto(self, "Crie um projeto antes de adicionar os arquivos!")
            return False


    # Função que irpa selecionar os arquivos com os dados
    def selecionar_arquivos(self):
        # Caixa de dialogo que irá permitir selecionar os arquivos
        # Este método me retorna uma lista com os caminhos de todos os arquivos selecionados
        arquivos_selecionados = QFileDialog().getOpenFileNames(self, 'Dados', '', 'Text files (*.exp)')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
