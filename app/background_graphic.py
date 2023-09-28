import sys
import os
from gui.window.py.JanelaBackground import *
from pyqtgraph import *
from pyqtgraph.Qt import QtGui, QtCore
import math


class BackgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.plot_widget = PlotWidget()
        self.curve = None
        self.conjunto_amostras = {}
        self.porcentagem_background = 0.2

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

        # Escodendo os elementos do menu (pois inicialmente ele está contraído)
        self.ui.frame.setVisible(False)

        # Chamando a função para expandir o menu
        self.ui.btn_ver_ajustes.clicked.connect(self.clique_botao)

        # Conectando a mudança de item na combobox com a atualização do gráfico
        self.ui.comboBox_arquivo_base.currentTextChanged.connect(self.atualizar_grafico)
        self.ui.comboBox_material_referencia.currentIndexChanged.connect(self.atualizar_grafico)


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

        # Esconda os elementos quando o menu estiver retraído (largura igual a 60)
        if largura_menu_esquerdo == 60:
            self.ui.frame.setVisible(True)
        else:
            self.ui.frame.setVisible(False)

    # Esses métodos são responsáveis por redimensionar e movimentar a janela
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
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

    def adicionar_dados(self, dados):
        self.conjunto_amostras = dados

    def preencher_combobox(self):
        self.ui.comboBox_arquivo_base.addItems(self.conjunto_amostras.keys())
        self.ui.comboBox_material_referencia.addItems(["172Yb", "173Yb", "175Lu", "176Hf",
                                                        "177Hf", "178Hf", "179Hf", "180Hf"])

    def plotar_grafico(self):
        # Plotando o gráfico
        self.ui.graphic_area.setLayout(QVBoxLayout())  # Crie um layout vertical no widget
        self.ui.graphic_area.layout().addWidget(self.plot_widget)  # Adicione o gráfico ao layout

        # Adicionando dados ao grafico

        # Obtendo o arquivo e o material que serão usados como modelos
        arquivo_base = self.ui.comboBox_arquivo_base.currentText()
        material_referencia = self.ui.comboBox_material_referencia.currentText()

        eixo_x = self.conjunto_amostras[arquivo_base]["Cycle"]
        eixo_y = self.conjunto_amostras[arquivo_base][material_referencia]

        #self.plot_widget.plot(eixo_x, eixo_y)
        self.plotar_dados(eixo_x, eixo_y)
        self.estilizar_grafico()




    def atualizar_grafico(self):
        arquivo = self.ui.comboBox_arquivo_base.currentText()
        material = self.ui.comboBox_material_referencia.currentText()

        if arquivo in self.conjunto_amostras and material in self.conjunto_amostras[arquivo]:
            eixo_x = self.conjunto_amostras[arquivo]["Cycle"]
            eixo_y = self.conjunto_amostras[arquivo][material]
            self.plotar_dados(eixo_x, eixo_y)
            self.estilizar_grafico()

        else:
            pass




    def plotar_dados(self, x, y):
        if self.plot_widget is not None:
            self.plot_widget.clear()
            self.curve = self.plot_widget.plot(x, y)
            self.definir_regiao_background_sinal()

    def definir_regiao_background_sinal(self):
        # Obtendo o número de pontos da amostra
        arquivo = self.ui.comboBox_arquivo_base.currentText()
        amostra = self.conjunto_amostras[arquivo]
        num_pontos = amostra.shape[0]

        pontos_a_retirar = math.ceil(num_pontos*self.porcentagem_background)

        inicio_background = 1
        final_background = pontos_a_retirar

        # Criando a região do background no gráfico
        # Crie uma região linear entre as duas linhas
        self.regiao_background = LinearRegionItem([inicio_background, final_background])
        self.regiao_background.setBrush(QBrush(QColor(255, 255, 255, 50)))
        self.plot_widget.addItem(self.regiao_background)

        inicio_sinal = final_background+1
        final_sinal = num_pontos-pontos_a_retirar

        # Crie uma região linear entre as duas linhas
        self.regiao_sinal = LinearRegionItem([inicio_sinal,final_sinal ])
        self.regiao_sinal.setBrush(QBrush(QColor(255, 255, 255, 50)))
        self.plot_widget.addItem(self.regiao_sinal)

    def estilizar_grafico(self):
        # Cor de fundo
        background_color = QColor(33, 37, 43)
        self.plot_widget.setBackground(background_color)

        # Título
        titulo = str(self.ui.comboBox_arquivo_base.currentText()) +"-"+ str(self.ui.comboBox_material_referencia.currentText())
        self.plot_widget.setTitle(titulo)

        # Titulo para os eixos
        self.plot_widget.setLabel('left', self.ui.comboBox_material_referencia.currentText(),color="grey", size=18)
        self.plot_widget.setLabel('bottom', "Cycle", color="grey", size=16)

        # Cor e espessura da linha
        self.curve.setPen(width=2)
        # Mude a cor da linha
        custom_color = mkPen(color=(85, 175, 207))
        self.curve.setPen(custom_color)

        # Adicionando um símbolo de pontos, aos pontos plotados
        self.curve.setSymbol('o')  # Use 'o' para representar cada ponto como um círculo
        self.curve.setSymbolPen(mkPen('b'))  # Defina a cor da borda do símbolo
        self.curve.setSymbolBrush(mkBrush('b'))  # Defina a cor do preenchimento do símbolo
        self.curve.setSymbolSize(5)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = BackgroundWindow()
    janela.show()
    sys.exit(app.exec())
