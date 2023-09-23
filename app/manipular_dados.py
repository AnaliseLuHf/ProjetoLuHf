# Esta classe irá filtrar os dados de entrada, retirando as linhas indesejadas dos arquivos
import os
import pandas as pd
class ManipularDadosArquivosOriginais():

    def excluir_dados_desnecessarios(self, arquivos, local, nome):

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
            nome_arquivo = local + "/" + nome + "/txt" + "/"+ f"{os.path.basename(arquivo_atual).replace('.exp','')}.txt"
            with open(nome_arquivo, 'w') as arquivo_destino:
                arquivo_destino.writelines(linhas)

    def criar_dataframes(self, arquivos):
        dataframes = {}
        for arquivo in arquivos:
            dataframes[os.path.basename(arquivo)] = pd.read_csv(arquivo, delimiter='\t', usecols=["Cycle","Time","172Yb","173Yb","175Lu","176Hf",
                                                                                                  "177Hf","178Hf","179Hf","180Hf","181Ta","178Hf/177Hf (1)",
                                                                                                  "180Hf/177Hf (2)","179Hf/177Hf (3)","172Yb/173Yb (4)",
                                                                                                  "176Hf/177Hf (5)","176Hf/177Hf (6)","181Ta/180Hf (7)",
                                                                                                  "175Lu/177Hf (8)","173Yb/177Hf (9)","172Yb/177Hf (10)"])

        return dataframes





