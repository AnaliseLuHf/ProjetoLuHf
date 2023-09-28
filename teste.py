import pyqtgraph as pg
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        # Crie um objeto PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.central_layout.addWidget(self.plot_widget)

        # Dados para o gráfico de exemplo
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 1, 3, 7]

        # Crie uma curva com os dados
        curve = self.plot_widget.plot(x, y)

        # Mude a espessura da linha
        curve.setPen(width=5)  # Defina a espessura da linha para 2 pixels

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
