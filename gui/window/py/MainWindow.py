from qt_core import *
from gui.resources.resources import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"/*	Propriedades globais, que se aplicam em toda interface*/\n"
"*{\n"
"	font-family:\"Segoe UI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"\n"
"/*	Propriedades da Central Widget*/\n"
"#centralwidget{\n"
"	background-color: #0F1526;\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"/*	Propriedades que se aplicam ao menu esquerdo*/\n"
"#leftMenuContent{\n"
"	background-color: #131931;\n"
"}\n"
"/*	Propriedades que se aplicam ao widget do conte\u00fado principal da janela*/\n"
"#bodyContent{\n"
"	background-color:#0F1526;\n"
"}\n"
"/*	Propriedades que se aplicam ao conteudo do cabe\u00e7alho da interface*/\n"
"#header_content{\n"
"	background-color:#182037;\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propri"
                        "edades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #169EF2 ;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Propriedades que se aplicam ao conte\u00fado do rodap\u00e9 na interface */\n"
"#footer_content{\n"
"	background-color:#182037;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es localizados ao menu esquerdo*/\n"
"#leftMenuContent QPushButton{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	font-size: 10pt;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#leftMenuContent QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam aos "
                        "bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#leftMenuContent .QPushButton:pressed {	\n"
"	background-color: #169EF2;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*	Propriedades que ser\u00e3o aplicadas ao frame que cont\u00e9m os bot\u00f5es de minimizar, maximizar e fechar janela*/\n"
"#frame_redm_janela QPushButton{\n"
"	background-color: transparent;\n"
"	background-position: center;\n"
"	background-repeat:none;\n"
"	border: none;\n"
"}\n"
"/*Criando um estilo para o bot\u00e3o que ir\u00e1 criar um novo projeto*/\n"
"#stackedWidget QPushButton{\n"
"	background-color:  #169EF2;\n"
"	background-repeat: none;\n"
"	background-position:center;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	font-size: 10pt;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"#stackedWidget QPushButton:hover{\n"
"	background-color:  rgba(255, 255, 255, 0.1);\n"
"}\n"
"#stackedWidget QPushButton:pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255,"
                        " 255, 255);\n"
"}\n"
"\n"
"#widget_novo_projeto{\n"
"	background-color:#1D2840 ;\n"
"	border-radius: 10px;\n"
"	\n"
"}\n"
"#widget_inicio{\n"
"	background-color: #1D2840;\n"
"	border-radius: 10px;\n"
"}\n"
"#widget_dados_arquivos{\n"
"	background-color: #1D2840;\n"
"}\n"
"\n"
"#frame_lista_arquivos{\n"
"	background-color: #0F1526;\n"
"	color: #495D7DE3;\n"
"}\n"
"\n"
"#frame_label_dados{\n"
"	background-color: #0F1526;\n"
"	color: #495D7DE3;\n"
"}\n"
"\n"
"\n"
"\n"
"/*Criando um estilo para os tooltips*/\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#0F1526 ;\n"
"	border: 1px solid  black;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LisWidget */\n"
"QListWidget {\n"
"	font: 10pt \"Segoe UI\";\n"
"    background-color: #1D2840;\n"
"    border: none ;\n"
""
                        "}\n"
"\n"
"/* Estilo para os itens na QListWidget */\n"
"QListWidget::item {\n"
"    color: #495D7DE3 ;\n"
"	margin: 2px; /* Ajuste o valor para controlar a margem dos itens */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo para os itens selecionados na QListWidget */\n"
"QListWidget::item:selected {\n"
"    background-color: #169EF2;\n"
"    color: #495D7DE3;\n"
"	border: none;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"TableWidget */\n"
"QTableWidget {	\n"
"	background-color: #0F1526 ;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid  rgb(40, 44, 52);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #169EF2;\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	gridline-color: #169EF2;\n"
"	color: white;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color:#169EF2 ;\n"
"}\n"
" QHeaderView::section{\n"
"	background-color: #131931;\n"
""
                        "	border: 1px solid  #131931;\n"
"	border-style: none;\n"
"    border-bottom: 1px solid  #131931;\n"
"    border-right: 1px solid  #131931;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:   #131931;\n"
"	color: #495D7DE3;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid  #131931;\n"
"	background-color:  #131931;\n"
"	padding: 3px;\n"
"	color: #495D7DE3;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"  	border: 1px solid  #131931;\n"
"	background-color:  #131931;\n"
"	padding-left: 10px;\n"
"	color: #495D7DE3;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color:  transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_content = QWidget(self.centralwidget)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 25))
        self.header_content.setMaximumSize(QSize(16777214, 25))
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 0, 0)
        self.label_nome_pag_atual = QLabel(self.header_content)
        self.label_nome_pag_atual.setObjectName(u"label_nome_pag_atual")
        self.label_nome_pag_atual.setStyleSheet(u"font: 12pt \"Bahnschrift Condensed\";\n"
"color: #495D7DE3\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label_nome_pag_atual)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_redm_janela = QFrame(self.header_content)
        self.frame_redm_janela.setObjectName(u"frame_redm_janela")
        self.frame_redm_janela.setFrameShape(QFrame.StyledPanel)
        self.frame_redm_janela.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_redm_janela)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_minimizar_janela = QPushButton(self.frame_redm_janela)
        self.btn_minimizar_janela.setObjectName(u"btn_minimizar_janela")
        self.btn_minimizar_janela.setMinimumSize(QSize(25, 25))
        self.btn_minimizar_janela.setMaximumSize(QSize(25, 25))
        self.btn_minimizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_minimize.png);")

        self.horizontalLayout_4.addWidget(self.btn_minimizar_janela)

        self.btn_maximizar_janela = QPushButton(self.frame_redm_janela)
        self.btn_maximizar_janela.setObjectName(u"btn_maximizar_janela")
        self.btn_maximizar_janela.setMinimumSize(QSize(25, 25))
        self.btn_maximizar_janela.setMaximumSize(QSize(25, 25))
        self.btn_maximizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_maximize.png);")

        self.horizontalLayout_4.addWidget(self.btn_maximizar_janela)

        self.btn_fechar_janela = QPushButton(self.frame_redm_janela)
        self.btn_fechar_janela.setObjectName(u"btn_fechar_janela")
        self.btn_fechar_janela.setMinimumSize(QSize(25, 25))
        self.btn_fechar_janela.setMaximumSize(QSize(25, 25))
        self.btn_fechar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_close.png);")

        self.horizontalLayout_4.addWidget(self.btn_fechar_janela)


        self.horizontalLayout.addWidget(self.frame_redm_janela, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_content, 0, Qt.AlignTop)

        self.app_content = QWidget(self.centralwidget)
        self.app_content.setObjectName(u"app_content")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_content.sizePolicy().hasHeightForWidth())
        self.app_content.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.app_content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContent = QWidget(self.app_content)
        self.leftMenuContent.setObjectName(u"leftMenuContent")
        self.leftMenuContent.setMinimumSize(QSize(0, 60))
        self.leftMenuContent.setMaximumSize(QSize(60, 16777215))
        self.leftMenuContent.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.leftMenuContent)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setStyleSheet(u"")
        self.frame_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_top_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy1)
        self.btn_menu.setMinimumSize(QSize(100, 45))
        self.btn_menu.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet(u"background-image: url(:/icones/icons/icon_menu.png);")

        self.verticalLayout_3.addWidget(self.btn_menu)


        self.verticalLayout_2.addWidget(self.frame_top_menu)

        self.frame_center_menu = QFrame(self.leftMenuContent)
        self.frame_center_menu.setObjectName(u"frame_center_menu")
        self.frame_center_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_center_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_center_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_inicio = QPushButton(self.frame_center_menu)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(100, 45))
        self.btn_inicio.setMaximumSize(QSize(16777215, 45))
        self.btn_inicio.setStyleSheet(u"background-image: url(:/icones/icons/cil-home.png);")

        self.verticalLayout_4.addWidget(self.btn_inicio)

        self.btn_pagina_novo_projeto = QPushButton(self.frame_center_menu)
        self.btn_pagina_novo_projeto.setObjectName(u"btn_pagina_novo_projeto")
        self.btn_pagina_novo_projeto.setMinimumSize(QSize(100, 45))
        self.btn_pagina_novo_projeto.setMaximumSize(QSize(16777215, 45))
        self.btn_pagina_novo_projeto.setStyleSheet(u"background-image: url(:/icones/icons/cil-folder.png);")

        self.verticalLayout_4.addWidget(self.btn_pagina_novo_projeto)

        self.btn_pagina_add_arquivos = QPushButton(self.frame_center_menu)
        self.btn_pagina_add_arquivos.setObjectName(u"btn_pagina_add_arquivos")
        self.btn_pagina_add_arquivos.setMinimumSize(QSize(100, 45))
        self.btn_pagina_add_arquivos.setMaximumSize(QSize(16777215, 45))
        self.btn_pagina_add_arquivos.setStyleSheet(u"background-image: url(:/icones/icons/cil-file.png);")

        self.verticalLayout_4.addWidget(self.btn_pagina_add_arquivos)

        self.pushButton_5 = QPushButton(self.frame_center_menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 45))
        self.pushButton_5.setMaximumSize(QSize(16777215, 45))
        self.pushButton_5.setStyleSheet(u"background-image: url(:/icones/icons/cil-arrow-bottom.png);")

        self.verticalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_center_menu)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.leftMenuContent)

        self.mainBodyContent = QWidget(self.app_content)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainBodyContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pagina_inicial = QWidget()
        self.pagina_inicial.setObjectName(u"pagina_inicial")
        self.verticalLayout_8 = QVBoxLayout(self.pagina_inicial)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.widget_inicio = QWidget(self.pagina_inicial)
        self.widget_inicio.setObjectName(u"widget_inicio")
        self.widget_inicio.setMinimumSize(QSize(600, 300))
        self.widget_inicio.setMaximumSize(QSize(600, 300))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_inicio)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_inicio)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-image: url(:/images/images/logo256x256edit-azul.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.widget_inicio)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(1, 0))
        self.frame_6.setMaximumSize(QSize(1, 240))
        self.frame_6.setStyleSheet(u"background-color: rgb(102, 101, 95);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.widget_inicio)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(65, -1, -1, -1)
        self.btn_novo_projeto_home = QPushButton(self.frame_5)
        self.btn_novo_projeto_home.setObjectName(u"btn_novo_projeto_home")
        self.btn_novo_projeto_home.setMinimumSize(QSize(150, 30))
        self.btn_novo_projeto_home.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.btn_novo_projeto_home)

        self.btn_abrir_projeto = QPushButton(self.frame_5)
        self.btn_abrir_projeto.setObjectName(u"btn_abrir_projeto")
        self.btn_abrir_projeto.setMinimumSize(QSize(150, 30))
        self.btn_abrir_projeto.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.btn_abrir_projeto)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.widget_inicio, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.pagina_inicial)
        self.pagina_add_arquivos = QWidget()
        self.pagina_add_arquivos.setObjectName(u"pagina_add_arquivos")
        self.horizontalLayout_3 = QHBoxLayout(self.pagina_add_arquivos)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_lista_arquivos = QWidget(self.pagina_add_arquivos)
        self.widget_lista_arquivos.setObjectName(u"widget_lista_arquivos")
        self.widget_lista_arquivos.setMinimumSize(QSize(200, 0))
        self.widget_lista_arquivos.setMaximumSize(QSize(200, 16777215))
        self.widget_lista_arquivos.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_lista_arquivos)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_lista_arquivos = QFrame(self.widget_lista_arquivos)
        self.frame_lista_arquivos.setObjectName(u"frame_lista_arquivos")
        self.frame_lista_arquivos.setMinimumSize(QSize(0, 25))
        self.frame_lista_arquivos.setMaximumSize(QSize(16777215, 25))
        self.frame_lista_arquivos.setStyleSheet(u"")
        self.frame_lista_arquivos.setFrameShape(QFrame.StyledPanel)
        self.frame_lista_arquivos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_lista_arquivos)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 0, 0, 0)
        self.label = QLabel(self.frame_lista_arquivos)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #495D7DE3;\n"
"font-size: 10pt;")

        self.verticalLayout_10.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_lista_arquivos)

        self.listWidget_lista_arquivos_importados = QListWidget(self.widget_lista_arquivos)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        QListWidgetItem(self.listWidget_lista_arquivos_importados)
        self.listWidget_lista_arquivos_importados.setObjectName(u"listWidget_lista_arquivos_importados")
        self.listWidget_lista_arquivos_importados.setMinimumSize(QSize(0, 300))
        self.listWidget_lista_arquivos_importados.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.listWidget_lista_arquivos_importados)

        self.widget = QWidget(self.widget_lista_arquivos)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 80))
        self.widget.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_12 = QVBoxLayout(self.widget)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_importar_dados = QPushButton(self.widget)
        self.btn_importar_dados.setObjectName(u"btn_importar_dados")
        self.btn_importar_dados.setMinimumSize(QSize(150, 30))
        self.btn_importar_dados.setMaximumSize(QSize(150, 30))

        self.verticalLayout_12.addWidget(self.btn_importar_dados, 0, Qt.AlignHCenter)

        self.btn_pg_corrigir_background = QPushButton(self.widget)
        self.btn_pg_corrigir_background.setObjectName(u"btn_pg_corrigir_background")
        self.btn_pg_corrigir_background.setMinimumSize(QSize(150, 30))
        self.btn_pg_corrigir_background.setMaximumSize(QSize(150, 30))

        self.verticalLayout_12.addWidget(self.btn_pg_corrigir_background, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.widget)


        self.horizontalLayout_3.addWidget(self.widget_lista_arquivos)

        self.widget_dados_arquivos = QWidget(self.pagina_add_arquivos)
        self.widget_dados_arquivos.setObjectName(u"widget_dados_arquivos")
        self.widget_dados_arquivos.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_dados_arquivos)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_label_dados = QFrame(self.widget_dados_arquivos)
        self.frame_label_dados.setObjectName(u"frame_label_dados")
        self.frame_label_dados.setMinimumSize(QSize(0, 25))
        self.frame_label_dados.setMaximumSize(QSize(16777215, 25))
        self.frame_label_dados.setStyleSheet(u"")
        self.frame_label_dados.setFrameShape(QFrame.StyledPanel)
        self.frame_label_dados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_label_dados)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.label_3 = QLabel(self.frame_label_dados)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #495D7DE3;\n"
"font-size: 10pt;")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_11.addWidget(self.frame_label_dados)

        self.tableWidget_tab_dados_brutos = QTableWidget(self.widget_dados_arquivos)
        if (self.tableWidget_tab_dados_brutos.columnCount() < 17):
            self.tableWidget_tab_dados_brutos.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        if (self.tableWidget_tab_dados_brutos.rowCount() < 19):
            self.tableWidget_tab_dados_brutos.setRowCount(19)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(12, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(13, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(14, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(15, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(16, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(17, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_tab_dados_brutos.setVerticalHeaderItem(18, __qtablewidgetitem35)
        self.tableWidget_tab_dados_brutos.setObjectName(u"tableWidget_tab_dados_brutos")
        self.tableWidget_tab_dados_brutos.setStyleSheet(u"color:#495D7DE3;\n"
"font: 10pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.tableWidget_tab_dados_brutos)


        self.horizontalLayout_3.addWidget(self.widget_dados_arquivos)

        self.stackedWidget.addWidget(self.pagina_add_arquivos)
        self.pagina_novo_projeto = QWidget()
        self.pagina_novo_projeto.setObjectName(u"pagina_novo_projeto")
        self.verticalLayout_7 = QVBoxLayout(self.pagina_novo_projeto)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.pagina_novo_projeto)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.footer_content = QWidget(self.mainBodyContent)
        self.footer_content.setObjectName(u"footer_content")
        self.footer_content.setMinimumSize(QSize(0, 25))
        self.footer_content.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.footer_content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 9)
        self.horizontalSpacer_2 = QSpacerItem(662, 4, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.footer_content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 15))
        self.label_2.setMaximumSize(QSize(60, 15))
        self.label_2.setStyleSheet(u"font-size: 9pt;\n"
"color:#495D7DE3;\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.footer_content, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.mainBodyContent)


        self.verticalLayout.addWidget(self.app_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_nome_pag_atual.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimizar_janela.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimizar_janela.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximizar_janela.setToolTip(QCoreApplication.translate("MainWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximizar_janela.setText("")
#if QT_CONFIG(tooltip)
        self.btn_fechar_janela.setToolTip(QCoreApplication.translate("MainWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fechar_janela.setText("")
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.btn_pagina_novo_projeto.setText(QCoreApplication.translate("MainWindow", u"Novo projeto", None))
        self.btn_pagina_add_arquivos.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 3", None))
        self.btn_novo_projeto_home.setText(QCoreApplication.translate("MainWindow", u"Novo projeto", None))
        self.btn_abrir_projeto.setText(QCoreApplication.translate("MainWindow", u"Abrir projeto", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Arquivos importados:", None))

        __sortingEnabled = self.listWidget_lista_arquivos_importados.isSortingEnabled()
        self.listWidget_lista_arquivos_importados.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_lista_arquivos_importados.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget_lista_arquivos_importados.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget_lista_arquivos_importados.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget_lista_arquivos_importados.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_lista_arquivos_importados.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_lista_arquivos_importados.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_lista_arquivos_importados.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget_lista_arquivos_importados.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.listWidget_lista_arquivos_importados.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget_lista_arquivos_importados.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget_lista_arquivos_importados.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget_lista_arquivos_importados.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem12 = self.listWidget_lista_arquivos_importados.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_lista_arquivos_importados.setSortingEnabled(__sortingEnabled)

        self.btn_importar_dados.setText(QCoreApplication.translate("MainWindow", u"Importar dados", None))
        self.btn_pg_corrigir_background.setText(QCoreApplication.translate("MainWindow", u"Corrigir background", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dados:", None))
        ___qtablewidgetitem = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem7 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem8 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem9 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem11 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem12 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem13 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem14 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem15 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem16 = self.tableWidget_tab_dados_brutos.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem17 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(13)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(14)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(15)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(16)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(17)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_tab_dados_brutos.verticalHeaderItem(18)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi

