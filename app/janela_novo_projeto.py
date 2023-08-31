from gui.window.py.NovoProjeto import *
import qt_core
import sys
from app.dialogs import *
from app.gerenciar_arquivos import *
from datetime import datetime

class JanelaNovoProjeto(QMainWindow):

    # Essas variáveis serão utilizadas para retornar, para a janela principal, o nome e o local onde o projeto foi salvo
    local_e_nome_projeto = Signal(str, str)

    def __init__(self):
        super().__init__()
        # Passa o caminho onde esta a pasta do projeto como um atributo. Assim, esse caminho pode ser usado por vários métodos.
        self.local_projeto = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Por padrão, o local será User>Desktop

        # Atributo para o nome do projeto, para que ele possa ser usado por outro métodos
        self.nome_projeto = "LuHf" + str(datetime.now())  # Por padrão, sera LuHF + Data e Hore quando foi criado

        self.caminho_projeto = self.local_projeto+"\\"+ self.nome_projeto

        self.ui = Ui_JanelaNovoProjeto()
        self.ui.setupUi(self)



        # Definindo um título para a janela
        self.setWindowTitle("Novo projeto")

        # Definindo um ícone
        self.setWindowIcon(QIcon("gui/images/icon.png"))

        # Conectando os botões as suas funções
        self.ui.btn_escolher_local_projeto.clicked.connect(self.selecionar_local_projeto)
        self.ui.btn_criar_projeto.clicked.connect(self.criar_projeto)

    def selecionar_local_projeto(self):
        dialog = QFileDialog()
        # Define para que seja escolhida apenas pastas
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec():
            # Pega o  caminho  da pasta que foi selecionada
            self.local_projeto = dialog.selectedFiles()[0]

        # Mostra o local selecionado no no campo label_local_projeto
        self.ui.label_local_projeto.setText(self.local_projeto)

    def criar_projeto(self):
        try:
            self.nome_projeto = self.ui.lineEdit_nome_do_projeto.text()
            self.local_projeto = self.ui.label_local_projeto.text()

            # Verificando se o local onde é inserido o nome do projeto e o local onde ficará salvo estão vazios
            if not self.nome_projeto.strip():
                # Se self.nome_projeto estiver vazio o nome padrão será Analise Lu e Hf + Data e Hora de criação
                nome_corrigido = "Análise Lu e Hf-" + str(datetime.now()).replace(':', '-').replace('.', '_')  # O nome precisa ser corrigido pois ele possui caracteres invalidos para os nomes das pastas (: e .)
                self.nome_projeto = nome_corrigido

            if not self.local_projeto.strip():
                # Se self.local_projeto estiver vazio o local padrão sera a pasta User>Desktop do PC
                self.local_projeto = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

            # Chamando o método da classe GerenciarArquivos, para criar a pasta com o nome e local desejado
            GerenciarArquivos.criar_pasta(self, local=self.local_projeto, nome_pasta=self.nome_projeto)

            # Se a criação da pasta do projeto teve exito
            mensagem = "Projeto criado com sucesso!"

            # Mostrando uma mensagem informando que o projeto foi criado
            DialogosSistema.msg_usuario(self, mensagem, tipo="Exito")

        # Se tiver algum erro durante a criação da pasta
        # Caso o local selecionado para salvar o projeto já tenha uma pasta como o nome escolhido
        except FileExistsError:
            mensagem = f"'{self.nome_projeto}' já existe em '{self.local_projeto}'"
            DialogosSistema.msg_usuario(self, mensagem, tipo="Erro")

        # Caso o usuário não possua acesso ao local selecionado para salvar o projeto
        except PermissionError:
            mensagem = f"Acesso restrito a '{self.local_projeto}'!"
            DialogosSistema.msg_usuario(self, mensagem, tipo="Erro")

        # Ou qualquer outro erro que apareça
        except:
            mensagem = "Erro!"
            DialogosSistema.msg_usuario(self, mensagem, tipo="Erro")

        # Após o projeto ter sido criado, o programa vai automaticamente para
        # a página para selecionar os arquivos com os dados
        #self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_add_arquivos)

        # Mostra o nome do projeto no header do programa
        '''self.ui.label_nome_projeto.setText(f"{self.nome_projeto}")'''

        # Mudando os atributos nome e local da classe
        self.caminho_projeto = self.local_projeto + "/"+ self.nome_projeto
        print(self.caminho_projeto)

        # Enviando o nome do projeto e o local onde ele esta salvo para a janela principal
        valor_local_projeto = self.local_projeto
        valor_nome_projeto = self.nome_projeto
        self.local_e_nome_projeto.emit(valor_local_projeto, valor_nome_projeto)



        # Cria as pastas necessárias para o projeto

        # Pasta onde ficará guardado os arquivos importados
        GerenciarArquivos.criar_pasta(self, self.caminho_projeto.replace("/", "\\"), "data")

        # Pasta onde ficará os arquivos após a filragem dos dados importantes
        GerenciarArquivos.criar_pasta(self, self.caminho_projeto.replace("/", "\\"), "txt")


        self.close()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaNovoProjeto()
    janela.show()
    sys.exit(app.exec())





