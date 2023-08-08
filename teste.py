import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class ColorChangingButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.button1 = QPushButton('Botão 1')
        self.button2 = QPushButton('Botão 2')
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

        # Conecta os sinais dos botões às funções de mudança de cor
        self.button1.clicked.connect(self.change_color_button1)
        self.button2.clicked.connect(self.change_color_button2)

        self.current_button = None  # Armazena o botão que foi clicado por último

        self.show()

    def change_color_button1(self):
        if self.current_button is not None:
            self.current_button.setStyleSheet('')  # Remove o estilo do botão anterior

        self.button1.setStyleSheet('background-color: red')  # Define a cor para o botão 1
        self.current_button = self.button1

    def change_color_button2(self):
        if self.current_button is not None:
            self.current_button.setStyleSheet('')  # Remove o estilo do botão anterior

        self.button2.setStyleSheet('background-color: blue')  # Define a cor para o botão 2
        self.current_button = self.button2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangingButtons()
    sys.exit(app.exec())
