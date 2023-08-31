# Esta classe irá filtrar os dados de entrada, retirando as linhas indesejadas dos arquivos
from app.gerenciar_arquivos import *
from main import MainWindow
import os
class FiltarDadosArquivosOriginais(MainWindow):

    def excluir_dados_desnecessarios(self, arquivos):

        linhas_a_pular_inicio = 22 # Linhas que contem os dados desnecessários no início
        linhas_a_pular_final = 13  # e no final

        for c in range(0, len(arquivos)):

            # Abrindo o arquivo original (da pasta data)
            arquivo_atual = arquivos[c]
            with open(arquivo_atual, "r") as arquivo:
                linhas = arquivo.readlines()

            # Excluindo as linhas com os dados desnessários
            linhas = linhas[linhas_a_pular_inicio: -linhas_a_pular_final]

            # Criando um novo arquivo, no formato txt, que ficará salvo na pasta "txt"
            nome_arquivo = self.local_projeto_criado + "/" + self.nome_projeto_criado + "/txt" + "/"+ f"{os.path.basename(arquivo_atual).replace('.exp','')}.txt"
            with open(nome_arquivo, 'w') as arquivo_destino:
                arquivo_destino.writelines(linhas)


