import sys
import os
from gui.window.py.JanelaBackground import *
from pyqtgraph import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import math
from app.dialogs import *

class BackgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.plot_widget = PlotWidget()
        self.curve = None
        self.dados_referencia = None


        # Setup a Main Window
        self.ui = Ui_BackgroundWindow()
        self.ui.setupUi(self)

        # Remove a barra de títulos padrão do Windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Redimensiona a janela
        QSizeGrip(self.ui.grid_resize)

        # Definindo a posição inicial do mouse (necessário para os eventos onde a tela é movida de posição)
        self.drag_start_position = None

        # Ativa o antiserrilhamento no gráfico
        pg.setConfigOptions(antialias=True)

        # Funções que minimiza, maximiza e fecha a janela
        self.ui.btn_fechar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_maximizar_janela.clicked.connect(self.clique_botao)
        self.ui.btn_minimizar_janela.clicked.connect(self.clique_botao)

        self.show()

    def clique_botao(self):
        # Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        # Pegando o nome do botão que foi clicado
        nome_botao = btn.objectName()

        # Expandir menu
        if nome_botao == "btn_ver_ajustes":
            self.expandir_menu()

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

    # Esses métodos são responsáveis por redimensionar e movimentar a janela
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            title_bar_height = self.ui.header_content.height()  # Ajuste isso para corresponder à altura da sua barra de título
            if event.y() <= title_bar_height:
                self.drag_start_position = event.globalPosition().toPoint() - self.pos()
                event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_start_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = None
            event.accept()

    # Este método evita que as regiões do background e sinal sejam movidas na vertical (pode sumir com os nomes das regiões no gráfico)
    '''def customMouseDragEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            # Ajusta a posição horizontal da região com base no movimento do mouse
            self.setRegion([self.getRegion()[0] + ev.pos().x() - ev.lastPos().x(),
                            self.getRegion()[1] + ev.pos().x() - ev.lastPos().x()])
            ev.accept()'''


    def plotar_grafico(self):
        # Plotando o gráfico
        self.ui.graphic_area.setLayout(QVBoxLayout())  # Crie um layout vertical no widget
        self.ui.graphic_area.layout().addWidget(self.plot_widget)  # Adicione o gráfico ao layout
        self.curve = self.plot_widget.plot([], [])  # Criar uma curva vazia

        self.estilizar_grafico()



    def adicionar_dados(self):
        dados = self.dados_referencia

        eixo_x = dados["Cycle"]
        eixo_y = dados["180Hf"]

        if self.curve is not None:  # Verificar se a curva já foi criada
            self.curve.setData(eixo_x, eixo_y)  # Atualizar os dados da curva
        else:
            self.curve = self.plot_widget.plot(eixo_x, eixo_y)  # Criar a curva se ainda não existir

        self.estilizar_grafico()  # Chamar estilizar_grafico() após criar ou atualizar a curve
        self.definir_background()

    def estilizar_grafico(self):
        # Cor de fundo
        background_color = QColor(33, 37, 43)
        self.plot_widget.setBackground(background_color)

        # Titulo para os eixos
        self.plot_widget.setLabel('left', 'Concentração',color="grey", size=18)
        self.plot_widget.setLabel('bottom', "Ciclo", color="grey", size=16)

        # Cor e espessura da linha
        self.curve.setPen(mkPen(color=(85, 175, 207), width=2))

        # Adicionando um símbolo de pontos, aos pontos plotados
        self.curve.setSymbol('o')  # Use 'o' para representar cada ponto como um círculo
        self.curve.setSymbolPen(mkPen(color=(85, 175, 207)))  # Defina a cor da borda do símbolo
        self.curve.setSymbolBrush(mkBrush(color=(85, 175, 207)))  # Defina a cor do preenchimento do símbolo
        self.curve.setSymbolSize(6)


    def definir_background(self):
        num_pontos = self.dados_referencia.shape[0]

        pontos_a_retirar = math.ceil(num_pontos * 0.1)

        inicio_background = 1
        limite_final_background = pontos_a_retirar

        # Criando a região do background no gráfico
        # Crie uma região linear entre as duas linhas
        self.regiao_background = LinearRegionItem([inicio_background, limite_final_background])
        self.regiao_background.setBrush(QBrush(QColor(255, 255, 255, 50)))
        self.regiao_background.setMovable(True)
        inicio_background = self.regiao_background.lines[0]  # Linha esquerda da região do background
        inicio_background.setBounds((1, 1))  # Sempre fixa em 1
        final_background = self.regiao_background.lines[1]  # Linha direita da região do background
        limite_sup_background = num_pontos - 1
        final_background.setBounds((1, limite_sup_background))
        self.plot_widget.addItem(self.regiao_background)

        #self.regiao_background.mouseDragEvent = lambda ev: self.customMouseDragEvent(self.regiao_background, ev)

        pg.InfLineLabel(self.regiao_background.lines[0], "Background", position=0.1, rotateAxis=(1, 0), anchor=(1, 1))

        inicio_sinal = limite_final_background + 1
        limite_final_sinal = num_pontos - pontos_a_retirar

        # Crie uma região linear entre as duas linhas
        self.regiao_sinal = LinearRegionItem([inicio_sinal, limite_final_sinal])
        self.regiao_sinal.setBrush(QBrush(QColor(255, 255, 255, 50)))
        inicio_sinal = self.regiao_sinal.lines[0]
        inicio_sinal.setBounds((2,num_pontos))
        final_sinal = self.regiao_sinal.lines[1]  # Linha direita da região do background
        final_sinal.setBounds((2, num_pontos))

        self.plot_widget.addItem(self.regiao_sinal)
        pg.InfLineLabel(self.regiao_sinal.lines[1], "Sinal", position=0.1, rotateAxis=(1, 0), anchor=(1, 1))

        # Conecte o sinal sigRegionChanged à função de callback
        self.regiao_background.sigRegionChanged.connect(self.obter_limites_background_sinal)
        self.regiao_sinal.sigRegionChanged.connect(self.obter_limites_background_sinal)

    # Função que pega os limites do sinal sempre que os limites da região for alterado
    def obter_limites_background_sinal(self):
        # Função chamada sempre que a região é alterada
        limites_background = self.regiao_background.getRegion()
        limites_sinal = self.regiao_sinal.getRegion()

        # Muda a cor da região, caso elas se sobreponham
        if limites_background[1] >= limites_sinal[0]:
            cor_da_regiao = QtGui.QBrush(QtGui.QColor(255, 0, 0, 50))  # Vermelho semi-transparente

        else:
            cor_da_regiao = QtGui.QBrush(QtGui.QColor(255, 255, 255, 50))

        self.regiao_background.setBrush(cor_da_regiao)


    def mostrar_mensagem_info(self, mensagem):
        dialog_info = DialogoInfo(mensagem)
        dialog_info.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = BackgroundWindow()
    janela.show()
    sys.exit(app.exec())
