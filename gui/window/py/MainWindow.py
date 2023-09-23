from qt_core import *
from gui.resources import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 574)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/*	Propriedades globais, que se aplicam em toda interface*/\n"
"*{\n"
"	font-family:\"Arial\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"\n"
"\n"
"/*	Propriedades da Central Widget*/\n"
"\n"
"/*	Propriedades que se aplicam ao menu esquerdo*/\n"
"#leftMenuContent{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"/*	Propriedades que se aplicam ao widget do conte\u00fado principal da janela*/\n"
"#bodyContent{\n"
"	background-color:#0F1526;\n"
"}\n"
"/*	Propriedades que se aplicam ao conteudo do cabe\u00e7alho da interface*/\n"
"#header_content{\n"
"	background-color:#21252B;\n"
"	border-bottom: 1px solid rgba(0,0,0,0.2);\n"
"	color: grey;\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	\n"
"}\n"
"\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam a"
                        "os bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #169EF2 ;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Propriedades que se aplicam ao conte\u00fado do rodap\u00e9 na interface */\n"
"#footer_content{\n"
"	background-color:#21252B;\n"
"	border-top: 1px solid rgba(0,0,0,0.2);\n"
"	color: grey;\n"
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
"	color: rgb(221, 221, 221);\n"
"	font-weight: bold;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#leftMenuContent QPushButton:hover{\n"
"	background-color:"
                        " rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#leftMenuContent .QPushButton:pressed {	\n"
"	background-color: #0254CF;\n"
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
"	background-color:  #55afcf;\n"
"	background-repeat: none;\n"
"	background-position:center;\n"
"	border: none;\n"
"	border-radius: 4px;\n"
"	font-size: 10pt;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"#stackedWidget QPushButton:hover{\n"
"	background-color:  rgba(255, 255, 255, 0.1);\n"
"}\n"
"#stackedWidget QPushButton"
                        ":pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#widget_inicio{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#widget_pg_add_arquivos_sup{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#widget_pg_add_arquivos_inf{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	\n"
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
"	background-color:#0F1526 ;\n"
"	border: 1px solid  black;\n"
"	border-radius: 5px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ListWidget */\n"
"QListWidget {\n"
"	background-color: rgb(44, 49, 58);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-radius: 10px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: "
                        "1px solid rgb(44, 49, 60);\n"
"	font: 11pt \"Arial\";\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background:  rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"}\n"
"QListWidget::item:selected{\n"
"	background-color:#55afcf;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	color: rgb(221,221,221);\n"
"	font-weight: bold;\n"
"	margin-right: 10px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"TableWidget */\n"
"QTableWidget {	\n"
"	background-color:  rgb(44, 49, 58);\n"
"	border-radius: 5px;\n"
"	border-bottom: 1px solid  rgb(40, 44, 52);\n"
"	font:\"Arial\";\n"
"	font-size: 10pt;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left:5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgba(255,255,255,0.1);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 1px solid  rgb(44, 49, 58);\n"
"	border-style: "
                        "none;\n"
"    border-bottom: 1px solid   rgb(33, 37, 43);\n"
"    border-right: 1px solid   rgb(33, 37, 43);\n"
"	color: rgb(221, 221, 221);\n"
"	font-weight: bold;\n"
"	font-size: 10pt;\n"
"}\n"
"QHeaderView::section:horizontal{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border: 1px solid  rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:   rgb(44, 49, 58);\n"
"	color: #ffb86c\n"
"}\n"
"QHeaderView::section:vertical{\n"
"  	border: 1px solid rgb(33, 37, 43);\n"
"	padding-left: 7px;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color:  transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	text-a"
                        "lign: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #55afcf;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScroll"
                        "Bar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #55afcf;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: mar"
                        "gin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QSplitter::handle {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_app = QFrame(self.centralwidget)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setStyleSheet(u"#container_app{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-radius: 4px;\n"
"}\n"
"")
        self.container_app.setFrameShape(QFrame.StyledPanel)
        self.container_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.container_app)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.header_content = QWidget(self.container_app)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 30))
        self.header_content.setMaximumSize(QSize(16777214, 30))
        self.header_content.setStyleSheet(u"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.label_titulo_programa = QLabel(self.header_content)
        self.label_titulo_programa.setObjectName(u"label_titulo_programa")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label_titulo_programa.setFont(font)
        self.label_titulo_programa.setStyleSheet(u"color:grey;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label_titulo_programa)

        self.label_nome_do_projeto = QLabel(self.header_content)
        self.label_nome_do_projeto.setObjectName(u"label_nome_do_projeto")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setItalic(True)
        self.label_nome_do_projeto.setFont(font1)
        self.label_nome_do_projeto.setStyleSheet(u"color:grey;")

        self.horizontalLayout.addWidget(self.label_nome_do_projeto)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_redm_janela = QFrame(self.header_content)
        self.frame_redm_janela.setObjectName(u"frame_redm_janela")
        self.frame_redm_janela.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 0px\n"
"}")
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
        self.btn_maximizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/cil-window-restore.png);")

        self.horizontalLayout_4.addWidget(self.btn_maximizar_janela)

        self.btn_fechar_janela = QPushButton(self.frame_redm_janela)
        self.btn_fechar_janela.setObjectName(u"btn_fechar_janela")
        self.btn_fechar_janela.setMinimumSize(QSize(25, 25))
        self.btn_fechar_janela.setMaximumSize(QSize(25, 25))
        self.btn_fechar_janela.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icones/icons/icon_close.png);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: red;\n"
"	border-top-right-radius: 2px;\n"
"	\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_fechar_janela)


        self.horizontalLayout.addWidget(self.frame_redm_janela)


        self.verticalLayout_16.addWidget(self.header_content)

        self.app_content = QWidget(self.container_app)
        self.app_content.setObjectName(u"app_content")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_content.sizePolicy().hasHeightForWidth())
        self.app_content.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.app_content)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContent = QWidget(self.app_content)
        self.leftMenuContent.setObjectName(u"leftMenuContent")
        self.leftMenuContent.setMinimumSize(QSize(60, 0))
        self.leftMenuContent.setMaximumSize(QSize(60, 16777215))
        self.leftMenuContent.setFont(font)
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
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_menu.setFont(font2)
        self.btn_menu.setStyleSheet(u"background-image: url(:/icones/icons/icon_menu.png);\n"
"")

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

        self.btn_add_arquivos = QPushButton(self.frame_center_menu)
        self.btn_add_arquivos.setObjectName(u"btn_add_arquivos")
        self.btn_add_arquivos.setMinimumSize(QSize(100, 45))
        self.btn_add_arquivos.setMaximumSize(QSize(16777215, 45))
        self.btn_add_arquivos.setStyleSheet(u"background-image: url(:/icones/icons/cil-file.png);")

        self.verticalLayout_4.addWidget(self.btn_add_arquivos)

        self.btn_pagina_visualizar_dados_arquivos = QPushButton(self.frame_center_menu)
        self.btn_pagina_visualizar_dados_arquivos.setObjectName(u"btn_pagina_visualizar_dados_arquivos")
        self.btn_pagina_visualizar_dados_arquivos.setMinimumSize(QSize(100, 45))
        self.btn_pagina_visualizar_dados_arquivos.setMaximumSize(QSize(16777215, 45))
        self.btn_pagina_visualizar_dados_arquivos.setStyleSheet(u"background-image: url(:/icones/icons/cil-screen-desktop.png);")

        self.verticalLayout_4.addWidget(self.btn_pagina_visualizar_dados_arquivos)

        self.btn_add_arquivos_adicionais = QPushButton(self.frame_center_menu)
        self.btn_add_arquivos_adicionais.setObjectName(u"btn_add_arquivos_adicionais")
        self.btn_add_arquivos_adicionais.setMinimumSize(QSize(100, 45))
        self.btn_add_arquivos_adicionais.setMaximumSize(QSize(16777215, 45))
        self.btn_add_arquivos_adicionais.setStyleSheet(u"background-image: url(:/icones/icons/cil-file-add.png);")

        self.verticalLayout_4.addWidget(self.btn_add_arquivos_adicionais)


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
        self.verticalLayout_8.setContentsMargins(-1, 0, 15, -1)
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
        self.frame_4.setStyleSheet(u"background-image: url(:/imagens/images/logo256x256edit-azul.png);")
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
        self.pagina_visualizar_dados_importados = QWidget()
        self.pagina_visualizar_dados_importados.setObjectName(u"pagina_visualizar_dados_importados")
        self.verticalLayout_7 = QVBoxLayout(self.pagina_visualizar_dados_importados)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.splitter = QSplitter(self.pagina_visualizar_dados_importados)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.widget_pg_add_arquivos_sup = QWidget(self.splitter)
        self.widget_pg_add_arquivos_sup.setObjectName(u"widget_pg_add_arquivos_sup")
        self.widget_pg_add_arquivos_sup.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_pg_add_arquivos_sup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.splitter_2 = QSplitter(self.widget_pg_add_arquivos_sup)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setHandleWidth(10)
        self.frame = QFrame(self.splitter_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setStyleSheet(u"background-color:  rgb(44, 49, 58);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)

        self.verticalLayout_11.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.lista_arquivos_importados = QListWidget(self.frame)
        self.lista_arquivos_importados.setObjectName(u"lista_arquivos_importados")
        self.lista_arquivos_importados.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_9.addWidget(self.lista_arquivos_importados)

        self.splitter_2.addWidget(self.frame)
        self.tabela_dados_originais = QTableWidget(self.splitter_2)
        self.tabela_dados_originais.setObjectName(u"tabela_dados_originais")
        self.tabela_dados_originais.setFocusPolicy(Qt.NoFocus)
        self.tabela_dados_originais.setStyleSheet(u"")
        self.tabela_dados_originais.setFrameShadow(QFrame.Sunken)
        self.tabela_dados_originais.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_dados_originais.setTextElideMode(Qt.ElideNone)
        self.tabela_dados_originais.setGridStyle(Qt.SolidLine)
        self.tabela_dados_originais.setCornerButtonEnabled(False)
        self.tabela_dados_originais.setRowCount(0)
        self.tabela_dados_originais.setColumnCount(0)
        self.splitter_2.addWidget(self.tabela_dados_originais)
        self.tabela_dados_originais.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_dados_originais.horizontalHeader().setMinimumSectionSize(50)
        self.tabela_dados_originais.horizontalHeader().setDefaultSectionSize(100)
        self.tabela_dados_originais.horizontalHeader().setStretchLastSection(True)
        self.tabela_dados_originais.verticalHeader().setVisible(False)
        self.tabela_dados_originais.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.splitter_2)

        self.splitter.addWidget(self.widget_pg_add_arquivos_sup)
        self.widget_pg_add_arquivos_inf = QWidget(self.splitter)
        self.widget_pg_add_arquivos_inf.setObjectName(u"widget_pg_add_arquivos_inf")
        self.widget_pg_add_arquivos_inf.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_pg_add_arquivos_inf)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 6)
        self.splitter_3 = QSplitter(self.widget_pg_add_arquivos_inf)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_3.setHandleWidth(10)
        self.frame_2 = QFrame(self.splitter_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setStyleSheet(u" background-color: rgb(44, 49, 58);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(6, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_12.addWidget(self.label_2)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.lista_arquivos_corrigidos = QListWidget(self.frame_2)
        self.lista_arquivos_corrigidos.setObjectName(u"lista_arquivos_corrigidos")
        self.lista_arquivos_corrigidos.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_10.addWidget(self.lista_arquivos_corrigidos)

        self.splitter_3.addWidget(self.frame_2)
        self.tabela_dados_corrigidos = QTableWidget(self.splitter_3)
        self.tabela_dados_corrigidos.setObjectName(u"tabela_dados_corrigidos")
        self.tabela_dados_corrigidos.setFocusPolicy(Qt.NoFocus)
        self.tabela_dados_corrigidos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_dados_corrigidos.setTextElideMode(Qt.ElideNone)
        self.tabela_dados_corrigidos.setCornerButtonEnabled(False)
        self.tabela_dados_corrigidos.setRowCount(0)
        self.tabela_dados_corrigidos.setColumnCount(0)
        self.splitter_3.addWidget(self.tabela_dados_corrigidos)
        self.tabela_dados_corrigidos.horizontalHeader().setMinimumSectionSize(50)
        self.tabela_dados_corrigidos.horizontalHeader().setDefaultSectionSize(100)
        self.tabela_dados_corrigidos.horizontalHeader().setStretchLastSection(True)
        self.tabela_dados_corrigidos.verticalHeader().setVisible(False)
        self.tabela_dados_corrigidos.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_6.addWidget(self.splitter_3)

        self.splitter.addWidget(self.widget_pg_add_arquivos_inf)

        self.verticalLayout_7.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.pagina_visualizar_dados_importados)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.mainBodyContent)


        self.verticalLayout_16.addWidget(self.app_content)

        self.footer_content = QFrame(self.container_app)
        self.footer_content.setObjectName(u"footer_content")
        self.footer_content.setMinimumSize(QSize(0, 20))
        self.footer_content.setMaximumSize(QSize(16777215, 20))
        self.footer_content.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.footer_content.setFrameShape(QFrame.StyledPanel)
        self.footer_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.size_grip = QFrame(self.footer_content)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setStyleSheet(u"background-image: url(:/icones/icons/cil-size-grip.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_16.addWidget(self.footer_content)


        self.verticalLayout.addWidget(self.container_app)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_titulo_programa.setText(QCoreApplication.translate("MainWindow", u"Lu&Hf An\u00e1lise de Dados -", None))
        self.label_nome_do_projeto.setText("")
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
#if QT_CONFIG(tooltip)
        self.btn_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.btn_inicio.setToolTip(QCoreApplication.translate("MainWindow", u"P\u00e1gina inicial", None))
#endif // QT_CONFIG(tooltip)
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
#if QT_CONFIG(tooltip)
        self.btn_pagina_novo_projeto.setToolTip(QCoreApplication.translate("MainWindow", u"Criar um projeto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pagina_novo_projeto.setText(QCoreApplication.translate("MainWindow", u"Novo projeto", None))
#if QT_CONFIG(tooltip)
        self.btn_add_arquivos.setToolTip(QCoreApplication.translate("MainWindow", u"Importar arquivos ao projeto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_arquivos.setText(QCoreApplication.translate("MainWindow", u"Importar arquivos", None))
#if QT_CONFIG(tooltip)
        self.btn_pagina_visualizar_dados_arquivos.setToolTip(QCoreApplication.translate("MainWindow", u"Ver dados importados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pagina_visualizar_dados_arquivos.setText(QCoreApplication.translate("MainWindow", u"Ver dados ", None))
#if QT_CONFIG(tooltip)
        self.btn_add_arquivos_adicionais.setToolTip(QCoreApplication.translate("MainWindow", u"Adicionar mais arquivos ao projeto atual", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_arquivos_adicionais.setText(QCoreApplication.translate("MainWindow", u"Adicionar arquivos", None))
        self.btn_novo_projeto_home.setText(QCoreApplication.translate("MainWindow", u"Novo projeto", None))
        self.btn_abrir_projeto.setText(QCoreApplication.translate("MainWindow", u"Abrir projeto", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DADOS ORIGINAIS:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DADOS CORRIGIDOS:", None))
    # retranslateUi

