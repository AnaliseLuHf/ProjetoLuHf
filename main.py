import sys
import os
import random
from gui.window.py.MainWindow import *
from gui.window.py.JanelaDeCarregamento import *
from app.gerenciar_arquivos import *  # Classe que gerencia a criação de pastas e arquivos do projeto
from app.dialogs import *  # Classe que gerencia as caixas de mensagem que aparecem
from app.janela_novo_projeto import *  # Classe que gerencia a janela para criar um projeto
from app.manipular_dados import *



# Classe que gerencia uma tela de carregamento para a aplicação
counter = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(100)

        dicas = ["Antes de importar os arquivos, crie um projeto!",
                 "O formato dos arquivos importados deve ser '.exp'!",
                 "Os arquivos importados são salvos na pasta do projeto!",
                 "Os arquivos importados são filtrados e convertidos para o formato '.txt'!"]
        # Change Texts
        QtCore.QTimer.singleShot(500, lambda: self.ui.label_dicas.setText("<strong>Importando</strong> DATABASE"))
        QtCore.QTimer.singleShot(1500,
                                 lambda: self.ui.label_dicas.setText("<strong>Carregando</strong> INTERFACE DE USUÁRIO"))
        QtCore.QTimer.singleShot(2500,
                                 lambda: self.ui.label_dicas.setText(f"<strong>DICA:</strong> {random.choice(dicas)} "))
        QtCore.QTimer.singleShot(5500,
                                 lambda: self.ui.label_dicas.setText(f"<strong>DICA:</strong> {random.choice(dicas)} "))
        QtCore.QTimer.singleShot(9000,
                                 lambda: self.ui.label_dicas.setText(f"<strong>DICA:</strong> {random.choice(dicas)} "))

        self.show()

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Atributos gerais da classe
        self.local_projeto_criado = None  # Guarda onde o projeto foi salvo
        self.nome_projeto_criado = None  # Guarda o nome do projeto
        self.caminho_pasta_data = None
        self.caminho_pasta_txt = None
        self.arquivos_selecionados = [] # Guarda o caminho dos arquivos importados
        self.arquivos_txt = [] # Guarda o caminho dos arquivos txt
        self.dataframes_arquivos_txt = {} # Dicionário, onde estão dos dataframes com os dados necessários de cada

        # arquivo importado

        # Setup a Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Esse objeto é responsável por adicionar a função de redimensionar a janela no canto inferior direito
        QSizeGrip(self.ui.size_grip)

        # Remove a barra de títulos padrão do Windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Definindo a posição inicial do mouse (necessário para os eventos onde a tela é movida de posição)
        self.drag_start_position = None

        # Definindo um ícone
        self.setWindowIcon(QIcon("gui/images/icon.png"))


        # Conectando o btn_menu a função que irá expandir/retrair o menu quando ele for clicado
        self.ui.btn_menu.clicked.connect(self.expandir_menu)
        # Conectando os botões do menu com as suas funções
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

        # Conectando o item selecionado das listas, para preencher a tabela com os dados
        self.ui.lista_arquivos_importados.itemClicked.connect(self.preencher_tab_arquivos_importados)

    # Essa função pega o nome do botão que foi clicado e conecta a uma "função" para ele
    def clique_botao(self):
        # Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        # Pegando o nome do botão que foi clicado
        nome_botao = btn.objectName()

        # Mostra a página inicial da aplicação
        if nome_botao == "btn_inicio":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_inicial)

        # Mostra a janela para criar um projeto
        if nome_botao == "btn_pagina_novo_projeto" or nome_botao == "btn_novo_projeto_home":

            # Abre a janela para criar um projeto
            self.jn_novo_projeto = JanelaNovoProjeto()

            # Muda os atributos da classe principal, pois a janela do novo projeto pega o
            # nome e o local do projeto escolhido pelo usuário
            self.jn_novo_projeto.local_e_nome_projeto.connect(self.mudar_atributos_classe)

            self.jn_novo_projeto.show()

        # Mostra a página para ver os arquivos carregados, já com os dados corrigidos do background
        if nome_botao == "btn_pagina_visualizar_dados_arquivos":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_visualizar_dados_importados)

        # Abre a caixa de diálogos para selecionar os arquivos
        if nome_botao == "btn_add_arquivos":
            # Verificando se já existem arquivos importados
            if len(self.arquivos_selecionados) > 0:
                # Caso já tenha arquivos importados, é mostrado na tela uma mensagem para continuar a importação (apagando os arquivos já importados) ou não
                mensagem = ("A importação de novos arquivos irá apagar os arquivos já importados."
                            " Caso queira adicionar mais arquivos, use a opção 'Adicionar arquivos adicionais'"
                            "Deseja continuar?")
                dialogo_interativo = DialogoInterativo(mensagem)
                dialogo_interativo.opcaoSelecionada.connect(self.obter_op_selecionada)
                dialogo_interativo.exec()

            else: # Se não existir, a função para adicionar os arquivos é chamada
                self.adicionar_arquivos()

        # Minimiza a janela da aplicação
        if nome_botao == "btn_minimizar_janela":
            self.showMinimized()

        # Maximiza a janela da aplicação
        if nome_botao == "btn_maximizar_janela":

            # Se a janela estiver no seu tamanho máximo, ele volta para o seu tamanho mínimo definido
            if self.isMaximized():
                self.showNormal()

            # Se a janela estiver no seu tamanho mínimo definido, ela é maximizada
            else:
                self.showMaximized()

        # Fecha a aplicação
        if nome_botao == "btn_fechar_janela":
            self.close()

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

    # Esses métodos são responsáveis por redimensionar e movimentar a janela
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_start_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = None
            event.accept()

    def mudar_atributos_classe(self, valor_local_projeto, valor_nome_projeto):
        self.local_projeto_criado = valor_local_projeto
        self.nome_projeto_criado = valor_nome_projeto

        # Mostra o nome do projeto no topo do programa
        self.ui.label_nome_do_projeto.setText(self.nome_projeto_criado)

    def limpar_atributos_classe(self):
        # Apagando os dados dos atributos da classe, que são preenchidos quando a função adicionar_arquivos é chamada
        self.arquivos_selecionados = []  # Guarda o caminho dos arquivos importados
        self.arquivos_txt = []  # Guarda o caminho dos arquivos txt
        self.dataframes_arquivos_txt = {}  # Dicionário, onde estão dos dataframes com os dados necessários de cada
        # arquivo importado

        # Apagando os arquivos já importados da pasta do projeto
        GerenciarArquivos.limpar_diretório(self, self.caminho_pasta_data)
        GerenciarArquivos.limpar_diretório(self, self.caminho_pasta_txt)


    # Como essa função é chamada apenas quando a opção clicada for "Sim", não é preciso fazer uma verificação da opção escolhida
    def obter_op_selecionada(self):
        # A partir desse ponto estava dando certo
        # Limpa os atributos da classe, que dependem dos arquivos importados
        self.limpar_atributos_classe()

        self.adicionar_arquivos()

    def verificar_projeto_criado(self):
        if self.local_projeto_criado is not None and self.nome_projeto_criado is not None:
            return True
        else:
            return False

    def adicionar_arquivos(self):

        status_projeto = self.verificar_projeto_criado()

        if status_projeto:
            # Chama a função que abre a caixa de diálogo para selecionar os arquivos
            arquivos_selecionados = self.selecionar_arquivos()

            # Copiando os arquivos selecionados para a pasta "data" do projeto
            self.caminho_pasta_data= self.local_projeto_criado + "/" + self.nome_projeto_criado + "/data"

            try:
                GerenciarArquivos.copiar_arquivos(self, arquivos_selecionados, self.caminho_pasta_data)

                # Pegando o caminho dos arquivos copiados para a pasta data, para passar como uma lista
                # sendo um atributo da classe
                caminhos_arquivos_data = []

                for arquivo in os.listdir(self.caminho_pasta_data):
                    caminho_arquivo = self.caminho_pasta_data + "/" + arquivo
                    if os.path.isfile(caminho_arquivo):
                        caminhos_arquivos_data.append(caminho_arquivo)

                # Mudando o atributo da classe, para uma lista com o nome dos arquivos selecionados
                self.arquivos_selecionados = caminhos_arquivos_data

                # Chamando a função que irá filtrar os dados originais, eliminando os dados desnecessários
                ManipularDadosArquivosOriginais.excluir_dados_desnecessarios(self, arquivos=self.arquivos_selecionados,
                                                                             local=self.local_projeto_criado, nome=self.nome_projeto_criado)

                # Mostrando os arquivos convertidos (exp para txt) em uma lista
                # Pegando o caminho da pasta txt
                self.caminho_pasta_txt = self.local_projeto_criado + "/" + self.nome_projeto_criado + "/txt"

                # Use a função os.listdir() para listar todos os itens na pasta (incluindo pastas)
                itens = os.listdir(self.caminho_pasta_txt)

                # Filtrar apenas os arquivos (não diretórios - retira alguma pasta, se houver).
                # Pegando os nomes dos arquivos
                nomes_arquivos_txt = [item for item in itens if os.path.isfile(os.path.join(self.caminho_pasta_txt, item))]

                # Colocando os caminhos dos arquivos txt como uma lista, que será um atributo da classe
                self.arquivos_txt = [self.caminho_pasta_txt + "/" + arquivo for arquivo in nomes_arquivos_txt]
                # Criando dataframes com os dados dos arquivos txt
                self.dataframes_arquivos_txt = ManipularDadosArquivosOriginais.criar_dataframes(self, self.arquivos_txt)

                # Passando os nomes para a função que irá os adicionar a lista
                self.preencher_listas(nomes_arquivos_txt, self.ui.lista_arquivos_importados)

                # Preenchendo a tabela com os dados do primeiro arquivo do dicionário de dataframes, assim que a os arquivos são importados
                self.preencher_tab_arquivos_importados(item=self.ui.lista_arquivos_importados.item(0))

                # Leva para a página para ver os dados dos arquivos
                self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_visualizar_dados_importados)

                print(f'Local: {self.local_projeto_criado} \n Nome: {self.nome_projeto_criado} \n Arquivos importados:{self.arquivos_selecionados}'
                      f'Arquivos txt: {self.arquivos_txt} \n Dataframes: {self.dataframes_arquivos_txt}')

            except Exception as e:
                message = f"{e}"
                dialog_erro = DialogoErro(message)
                dialog_erro.exec()

        else:
            message = "Crie um projeto antes de importar os arquivos!"
            dialog_info = DialogoInfo(message)
            dialog_info.exec()

    def selecionar_arquivos(self):
        while True:
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)

            # Mostra apenas os arquivos com extensão ".exp"
            file_dialog.setNameFilter("Arquivos de Texto (*.exp);")

            if file_dialog.exec():
                # Obtenha os arquivos selecionados
                arquivos_selecionados = file_dialog.selectedFiles()

                if arquivos_selecionados:
                    return arquivos_selecionados

                else:
                    return None  # O usuário cancelou a operação


    # Função que irá preencher as listas do programa com os arquivos
    def preencher_listas(self, itens_lista, lista):
        # Verificando se existem itens na lista. Se sim, eles são excluídos

        if lista.count() > 0:
            lista.clear()

        for arquivo in itens_lista:
            list_item = QListWidgetItem(arquivo)
            lista.addItem(list_item)

        # Deixa o primeiro item da lista já selecionado ( vai auxiliar para preencher automaticamente
        # a tabela com os dados importados)
        lista.setCurrentRow(0)


    def preencher_tab_arquivos_importados(self, item):
        # Obtendo o item selecionado atual da lista Arquivos importados
        item_selecionado = item.text()

        # Obtendo os dados do arquivo selecionado anteriormente (item selecionado na lista), do dicionário de dataframe
        dados = self.dataframes_arquivos_txt[item_selecionado]

        # Obtendo o número de linhas e colunas do dataframe
        num_linhas = len(dados)
        num_colunas = len(dados.columns)

        # Configurando o número de linhas e coluna da tabela
        self.ui.tabela_dados_originais.setRowCount(num_linhas)
        self.ui.tabela_dados_originais.setColumnCount(num_colunas)

        # ENCONTRANDO O NOME DAS COLUNAS
        nome_das_colunas = dados.columns.tolist()
        self.ui.tabela_dados_originais.setHorizontalHeaderLabels(nome_das_colunas)

        # Adicionando itens à tabela
        for linha in range(num_linhas):
            for coluna in range(num_colunas):
                self.ui.tabela_dados_originais.setItem(linha, coluna, QTableWidgetItem(
                    str(dados.iloc[linha][coluna])))

        # Redimensiona o tamanho das colunas para mostrar os dados com o tamanho correto
        self.ui.tabela_dados_originais.resizeColumnsToContents()

    def mostrar_mensagem_exito(self):
        message = f"Projeto criado com sucesso em:{self.caminho_projeto}"
        dialog = DialogoExito(message)
        dialog.exec()

    def mostrar_mensagem_erro(self, mensagem):
        message = f"{mensagem}"
        dialog_erro = DialogoErro(message)
        dialog_erro.exec()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
