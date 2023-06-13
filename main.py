import sys
import os
from qt_core import *
from gui.window.ui.main_window import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup a Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Definindo um título para a janela
        self.setWindowTitle("LuHf")

        # Exibindo a janela
        self.show()

        # Conectando o btn_menu a função que irá expandir/retrair o menu quando ele for clicado
        self.ui.btn_menu.clicked.connect(self.expandir_menu)


    # Função que irá expandir e retrair o menu esquerdo
    def expandir_menu(self):
        # Pegando a largura do menu esquerdo
        largura_menu_esquerdo = self.ui.leftMenuContent.width()

        largura_padrao = 60

        if largura_menu_esquerdo == 60:
            largura_padrao = 150

        #Animando a transição
        self.animation = QPropertyAnimation(self.ui.leftMenuContent, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(largura_menu_esquerdo)
        self.animation.setEndValue(largura_padrao)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
