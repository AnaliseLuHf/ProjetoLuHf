

# Classe que irá realizar as correções e calculos necessários
class CalcularCorrecoes:
    # Método que irá realizar a separação entre background e sinal
    def corrigir_background_sinal(self, conjunto_dados):
        # Elemento que será usado como referência
        col_parametro = "180Hf"
        sinal_separado = {}
        background_separado = {}
        media_sinal = {}
        media_background = {}

        # Dicionário que irá armazenar o limite de cada arquivo
        limite_background_sinal = {}

        # ACESSANDO OS DADOS BRUTOS
        for nome, data in conjunto_dados.items():
            media_col_parametro = data[col_parametro].mean()  # Fazendo a média da coluna passada como parâmetro
            # Contador para o índice da linha onde tem o limite sinal/background
            index_limite = 0
            limite = 0 # Limite background/sinal
            # Comparando o valor de cada linha da coluna parâmetro com a média
            for valor in data[col_parametro]:
                if valor > media_col_parametro:
                    # Salvando o índice da linha onde há o limite
                    limite = index_limite
                    limite_background_sinal[nome] = limite
                    break
                else:
                    # Atualizando o contador do limite
                    index_limite += 1

            # Verificar o índice definido
            # Número de linha de cada arquivo
            numero_linhas = len(data.index)
            if limite == 0 or limite == numero_linhas:
                limite = numero_linhas // 2

            # Calculando a % subtraída do background
            porcentagem_subtraida_background = int(round((limite * 0.3), 0))  # Definido 30% de background [Apenas testes]
            # Separando os dados de background (retirandoa coluna "Cycle")
            background = data.iloc[porcentagem_subtraida_background:(limite - porcentagem_subtraida_background), 1:]
            # Média dos pontos de background
            media_bk = background.mean()
            # Salvando o background separado
            background_separado[nome] = background
            # Salvando a média do background
            media_background[nome] = media_bk

            # Calculando a % subtraída do sinal
            porcentagem_subtraida_sinal = int(round(((numero_linhas - limite) * 0.05), 0))  # Definindo 5% de sinal
            sinal = data.iloc[(limite + porcentagem_subtraida_sinal):(numero_linhas - porcentagem_subtraida_sinal), 1:]
            # Fazendo a média do sinal
            media_sg = sinal.mean()
            # Salvando os dados separados
            sinal_separado[nome] = sinal
            # Salvando os dados separados
            media_sinal[nome] = media_sg

        # Retornado as variáveis
        return sinal_separado, background_separado, media_background, media_sinal, limite_background_sinal









