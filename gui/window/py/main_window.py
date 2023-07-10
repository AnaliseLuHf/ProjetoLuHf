from qt_core import *
from gui.resources import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 506)
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
"	background-color:#17181A;\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"/*	Propriedades que se aplicam ao menu esquerdo*/\n"
"#leftMenuContent{\n"
"	background-color: #202123;\n"
"}\n"
"/*	Propriedades que se aplicam ao widget do conte\u00fado principal da janela*/\n"
"#bodyContent{\n"
"	background-color:#17181A;\n"
"}\n"
"/*	Propriedades que se aplicam ao conteudo do cabe\u00e7alho da interface*/\n"
"#header_content{\n"
"	background-color:#025939;\n"
"	color: white;\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
""
                        "/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #04BF7B;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*	Propriedades que se aplicam ao conte\u00fado do rodap\u00e9 na interface */\n"
"#footer_content{\n"
"	background-color:#025939;\n"
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
"	font-weight: bold;\n"
"	color: #acacac;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#leftMenuContent QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"/*	Pr"
                        "opriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#leftMenuContent .QPushButton:pressed {	\n"
"	background-color: #04BF7B;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuContent .QPushButton:checked{\n"
"	background-color: red;\n"
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
"	background-color:  transparent;\n"
"	background-repeat: none;\n"
"	background-position:center;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	font-size: 10pt;\n"
"	font-weight: bold;\n"
"	color: #acacac;\n"
"}\n"
"#stackedWidget QPushButton:hover{\n"
"	background-color:  rgb(40, 44"
                        ", 52);\n"
"}\n"
"#stackedWidget QPushButton:pressed{\n"
"	background-color: #025939;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#widget_novo_projeto{\n"
"	background-color: #202123;\n"
"	border-radius: 10px;\n"
"}\n"
"#widget_inicio{\n"
"	background-color: #202123;\n"
"	border-radius: 10px\n"
"}\n"
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
"	background-color: #202123 ;\n"
"	border: 1px solid  black;\n"
"	border-radius: 5px;\n"
"\n"
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
        self.header_content.setMinimumSize(QSize(0, 40))
        self.header_content.setMaximumSize(QSize(16777214, 40))
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.header_content)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(50, 50))
        self.frame_logo.setMaximumSize(QSize(50, 50))
        self.frame_logo.setStyleSheet(u"background-image: url(:/images/images/logo50x50.png);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)

        self.horizontalLayout.addWidget(self.frame_logo, 0, Qt.AlignLeft)

        self.label_nome_projeto = QLabel(self.header_content)
        self.label_nome_projeto.setObjectName(u"label_nome_projeto")
        self.label_nome_projeto.setStyleSheet(u"font-size: 9pt;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_nome_projeto)

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
        self.btn_minimizar_janela.setMinimumSize(QSize(28, 28))
        self.btn_minimizar_janela.setMaximumSize(QSize(28, 28))
        self.btn_minimizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_minimize.png);")

        self.horizontalLayout_4.addWidget(self.btn_minimizar_janela)

        self.btn_maximizar_janela = QPushButton(self.frame_redm_janela)
        self.btn_maximizar_janela.setObjectName(u"btn_maximizar_janela")
        self.btn_maximizar_janela.setMinimumSize(QSize(28, 28))
        self.btn_maximizar_janela.setMaximumSize(QSize(28, 28))
        self.btn_maximizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_maximize.png);")

        self.horizontalLayout_4.addWidget(self.btn_maximizar_janela)

        self.btn_fechar_janela = QPushButton(self.frame_redm_janela)
        self.btn_fechar_janela.setObjectName(u"btn_fechar_janela")
        self.btn_fechar_janela.setMinimumSize(QSize(28, 28))
        self.btn_fechar_janela.setMaximumSize(QSize(28, 28))
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
        self.horizontalLayout_9 = QHBoxLayout(self.pagina_inicial)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_inicio = QWidget(self.pagina_inicial)
        self.widget_inicio.setObjectName(u"widget_inicio")
        self.widget_inicio.setMinimumSize(QSize(500, 250))
        self.widget_inicio.setMaximumSize(QSize(500, 250))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_inicio)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_inicio)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-image: url(:/images/images/logo256x256edit.png);")
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
        self.btn_novo_projeto_home = QPushButton(self.frame_5)
        self.btn_novo_projeto_home.setObjectName(u"btn_novo_projeto_home")
        self.btn_novo_projeto_home.setMinimumSize(QSize(150, 30))
        self.btn_novo_projeto_home.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.btn_novo_projeto_home, 0, Qt.AlignHCenter)

        self.btn_abrir_projeto = QPushButton(self.frame_5)
        self.btn_abrir_projeto.setObjectName(u"btn_abrir_projeto")
        self.btn_abrir_projeto.setMinimumSize(QSize(150, 30))
        self.btn_abrir_projeto.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.btn_abrir_projeto, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.frame_5)


        self.horizontalLayout_9.addWidget(self.widget_inicio)

        self.stackedWidget.addWidget(self.pagina_inicial)
        self.pagina_add_arquivos = QWidget()
        self.pagina_add_arquivos.setObjectName(u"pagina_add_arquivos")
        self.btn_add_arquivos_dados = QPushButton(self.pagina_add_arquivos)
        self.btn_add_arquivos_dados.setObjectName(u"btn_add_arquivos_dados")
        self.btn_add_arquivos_dados.setGeometry(QRect(574, 380, 91, 24))
        self.stackedWidget.addWidget(self.pagina_add_arquivos)
        self.pagina_novo_projeto = QWidget()
        self.pagina_novo_projeto.setObjectName(u"pagina_novo_projeto")
        self.verticalLayout_7 = QVBoxLayout(self.pagina_novo_projeto)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_novo_projeto = QWidget(self.pagina_novo_projeto)
        self.widget_novo_projeto.setObjectName(u"widget_novo_projeto")
        self.widget_novo_projeto.setMinimumSize(QSize(600, 300))
        self.widget_novo_projeto.setMaximumSize(QSize(600, 300))
        self.widget_novo_projeto.setStyleSheet(u"\n"
"font-size: 10pt;\n"
"font-weight: bold;\n"
"color: #acacac;")
        self.verticalLayout_8 = QVBoxLayout(self.widget_novo_projeto)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.widget_novo_projeto)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget)

        self.frame_2 = QFrame(self.widget_novo_projeto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_nome_projeto = QLineEdit(self.frame_2)
        self.lineEdit_nome_projeto.setObjectName(u"lineEdit_nome_projeto")
        self.lineEdit_nome_projeto.setMinimumSize(QSize(500, 0))
        self.lineEdit_nome_projeto.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_nome_projeto)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame = QFrame(self.widget_novo_projeto)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.label_local_projeto = QLabel(self.frame)
        self.label_local_projeto.setObjectName(u"label_local_projeto")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_local_projeto.sizePolicy().hasHeightForWidth())
        self.label_local_projeto.setSizePolicy(sizePolicy3)
        self.label_local_projeto.setMinimumSize(QSize(450, 20))
        self.label_local_projeto.setMaximumSize(QSize(450, 20))
        self.label_local_projeto.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")

        self.horizontalLayout_7.addWidget(self.label_local_projeto)

        self.btn_selecionar_local_projeto = QPushButton(self.frame)
        self.btn_selecionar_local_projeto.setObjectName(u"btn_selecionar_local_projeto")
        self.btn_selecionar_local_projeto.setMinimumSize(QSize(30, 30))
        self.btn_selecionar_local_projeto.setMaximumSize(QSize(30, 30))
        self.btn_selecionar_local_projeto.setStyleSheet(u"background-image: url(:/icones/icons/cil-folder.png);")

        self.horizontalLayout_7.addWidget(self.btn_selecionar_local_projeto)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_3 = QFrame(self.widget_novo_projeto)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_criar_projeto = QPushButton(self.frame_3)
        self.btn_criar_projeto.setObjectName(u"btn_criar_projeto")
        self.btn_criar_projeto.setMinimumSize(QSize(100, 30))
        self.btn_criar_projeto.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.btn_criar_projeto)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.widget_novo_projeto, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.pagina_novo_projeto)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.footer_content = QWidget(self.mainBodyContent)
        self.footer_content.setObjectName(u"footer_content")
        self.footer_content.setMinimumSize(QSize(0, 25))
        self.footer_content.setMaximumSize(QSize(16777215, 25))
        self.label_2 = QLabel(self.footer_content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 0, 75, 25))
        self.label_2.setMinimumSize(QSize(75, 20))
        self.label_2.setMaximumSize(QSize(75, 16777215))
        self.label_2.setStyleSheet(u"font-size: 9pt;\n"
"color: white;\n"
"font-weight: bold;\n"
"")

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
        self.label_nome_projeto.setText("")
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
        self.btn_add_arquivos_dados.setText(QCoreApplication.translate("MainWindow", u"Add Arquivos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Novo projeto:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Local: ", None))
        self.label_local_projeto.setText("")
        self.btn_selecionar_local_projeto.setText("")
        self.btn_criar_projeto.setText(QCoreApplication.translate("MainWindow", u"Criar projeto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi

