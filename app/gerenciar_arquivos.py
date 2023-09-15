# Esta classe irá gerenciar a criação, exclusão, manipular arquivos gerados pelo programa, quando necessário
import os
import shutil

class GerenciarArquivos:
    # Esse método cria uma pasta sempre que ele for chamado
    def criar_pasta(self, local, nome_pasta):
        caminho = os.path.join(local, nome_pasta)
        os.makedirs(caminho)

    # Verfica se uma pasta existe
    def verificar_pasta(self, nome_pasta):
        # Verifica se o caminho existe e é uma pasta
        if os.path.exists(nome_pasta) and os.path.isdir(nome_pasta):
            return True

        else:
            return False

    def copiar_arquivos(self, caminho_origem, caminho_destino):
        for c in range (0, len(caminho_origem)):
            caminho_original = caminho_origem[c]
            caminho_final = caminho_destino
            shutil.copy(caminho_original, caminho_final)

    def limpar_diretório(self, caminho_diretorio):
        # Listar todos os arquivos no diretório
        arquivos = os.listdir(caminho_diretorio)

        # Iterar sobre os arquivos e excluí-los
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_diretorio, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)






