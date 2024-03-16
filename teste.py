#import pyqtgraph.examples
#pyqtgraph.examples.run()

import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg

def regionChanged():
    # Esta função será chamada quando a região for movida
    print("Posição da linha inicial:", regiao_background.getRegion()[0])
    print("Posição da linha final:", regiao_background.getRegion()[1])

def main():
    # Crie uma aplicação Qt
    app = QApplication(sys.argv)

    # Crie um widget de plotagem
    plot_widget = pg.plot()

    # Defina os valores inicial e final para a região
    inicio_background = 1
    final_background = 5

    # Crie a região linear
    global regiao_background
    regiao_background = pg.LinearRegionItem([inicio_background, final_background])
    regiao_background.setBrush(pg.mkBrush(255, 255, 255, 50))
    plot_widget.addItem(regiao_background)

    # Conecte o sinal sigRegionChangeFinished ao slot regionChanged
    regiao_background.sigRegionChangeFinished.connect(regionChanged)

    # Exiba o widget de plotagem
    plot_widget.show()

    # Feche a aplicação quando a janela for fechada
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
