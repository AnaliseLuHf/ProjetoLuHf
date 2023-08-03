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

    def copiar_arquvos(self, caminho_origem, caminho_destino):
        for c in range (0, len(caminho_origem)):
            caminho_original = caminho_origem[c]
            caminho_final = caminho_destino
            shutil.copy(caminho_original, caminho_final)





