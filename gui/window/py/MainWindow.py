from qt_core import *
from gui.resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setStyleSheet(u"/*	Propriedades globais, que se aplicam em toda interface*/\n"
"*{\n"
"	font-family:\"Arial\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"\n"
"/*	Propriedades da Central Widget*/\n"
"#centralwidget{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-radius:10px;\n"
"}\n"
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
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	backgroun"
                        "d-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #169EF2 ;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Propriedades que se aplicam ao conte\u00fado do rodap\u00e9 na interface */\n"
"#footer_content{\n"
"	background-color:#2C313A;\n"
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
"	font-size: 9pt;\n"
"	color: grey;\n"
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
"#left_content_pg_add_arquivos{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#right_content_pg_add_arquivos{\n"
"	border-radius: 5px;\n"
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
""
                        "	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
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
"	background-color: rgb(33, 37, 43);\n"
"	border: 1px solid  rgb(44"
                        ", 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid   rgb(33, 37, 43);\n"
"    border-right: 1px solid   rgb(33, 37, 43);\n"
"	color: rgb(221, 221, 221);\n"
"	font-weight: bold;\n"
"	font-size: 10pt;\n"
"}\n"
"QHeaderView::section:horizontal{\n"
"    border: 1px solid  rgb(33, 37, 43);\n"
"	padding: 3px;\n"
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
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"/* /"
                        "////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
""
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
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow"
                        ":vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
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
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.label_nome_pag_atual = QLabel(self.header_content)
        self.label_nome_pag_atual.setObjectName(u"label_nome_pag_atual")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label_nome_pag_atual.setFont(font)
        self.label_nome_pag_atual.setStyleSheet(u"color:grey;\n"
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
        self.btn_maximizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/cil-window-restore.png);")

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
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.btn_menu.setFont(font1)
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
        self.pagina_add_arquivos = QWidget()
        self.pagina_add_arquivos.setObjectName(u"pagina_add_arquivos")
        self.horizontalLayout_3 = QHBoxLayout(self.pagina_add_arquivos)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_content_pg_add_arquivos = QWidget(self.pagina_add_arquivos)
        self.left_content_pg_add_arquivos.setObjectName(u"left_content_pg_add_arquivos")
        self.left_content_pg_add_arquivos.setMinimumSize(QSize(250, 0))
        self.left_content_pg_add_arquivos.setMaximumSize(QSize(250, 16777215))
        self.left_content_pg_add_arquivos.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.left_content_pg_add_arquivos)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.left_content_pg_add_arquivos)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(150, 30))
        self.frame_7.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_5)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.frame = QFrame(self.left_content_pg_add_arquivos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lista_arquivos_imprtados = QListWidget(self.frame)
        self.lista_arquivos_imprtados.setObjectName(u"lista_arquivos_imprtados")
        self.lista_arquivos_imprtados.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_11.addWidget(self.lista_arquivos_imprtados)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.lista_arquivos_corrigidos = QListWidget(self.frame)
        self.lista_arquivos_corrigidos.setObjectName(u"lista_arquivos_corrigidos")
        self.lista_arquivos_corrigidos.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_11.addWidget(self.lista_arquivos_corrigidos)


        self.verticalLayout_10.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.left_content_pg_add_arquivos)

        self.right_content_pg_add_arquivos = QWidget(self.pagina_add_arquivos)
        self.right_content_pg_add_arquivos.setObjectName(u"right_content_pg_add_arquivos")
        self.right_content_pg_add_arquivos.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.right_content_pg_add_arquivos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_area_dados_originais = QWidget(self.right_content_pg_add_arquivos)
        self.widget_area_dados_originais.setObjectName(u"widget_area_dados_originais")
        self.widget_area_dados_originais.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_area_dados_originais)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_area_dados_originais)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(150, 30))
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_3)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.tabela_dados_originais = QTableWidget(self.widget_area_dados_originais)
        self.tabela_dados_originais.setObjectName(u"tabela_dados_originais")
        self.tabela_dados_originais.setFocusPolicy(Qt.NoFocus)
        self.tabela_dados_originais.setStyleSheet(u"")
        self.tabela_dados_originais.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_dados_originais.setShowGrid(True)
        self.tabela_dados_originais.setWordWrap(True)
        self.tabela_dados_originais.setCornerButtonEnabled(False)
        self.tabela_dados_originais.horizontalHeader().setStretchLastSection(False)
        self.tabela_dados_originais.verticalHeader().setVisible(False)
        self.tabela_dados_originais.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.tabela_dados_originais)


        self.verticalLayout_7.addWidget(self.widget_area_dados_originais)

        self.widget_dados_corrigidos_background = QWidget(self.right_content_pg_add_arquivos)
        self.widget_dados_corrigidos_background.setObjectName(u"widget_dados_corrigidos_background")
        self.widget_dados_corrigidos_background.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_dados_corrigidos_background)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget_dados_corrigidos_background)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(150, 30))
        self.frame_3.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_4)


        self.verticalLayout_15.addWidget(self.frame_3)

        self.tableWidget_2 = QTableWidget(self.widget_dados_corrigidos_background)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.setRowCount(0)

        self.verticalLayout_15.addWidget(self.tableWidget_2)


        self.verticalLayout_7.addWidget(self.widget_dados_corrigidos_background)


        self.horizontalLayout_3.addWidget(self.right_content_pg_add_arquivos)

        self.stackedWidget.addWidget(self.pagina_add_arquivos)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.footer_content = QWidget(self.mainBodyContent)
        self.footer_content.setObjectName(u"footer_content")
        self.footer_content.setMinimumSize(QSize(0, 20))
        self.footer_content.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.footer_content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 4, 0, 9)
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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_nome_pag_atual.setText(QCoreApplication.translate("MainWindow", u"Lu&Hf Data Analysis", None))
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
        self.btn_add_arquivos.setToolTip(QCoreApplication.translate("MainWindow", u"Adicionar arquivos ao projeto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_arquivos.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 3", None))
#if QT_CONFIG(tooltip)
        self.btn_pagina_visualizar_dados_arquivos.setToolTip(QCoreApplication.translate("MainWindow", u"Ver dados importados", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pagina_visualizar_dados_arquivos.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 2", None))
        self.btn_novo_projeto_home.setText(QCoreApplication.translate("MainWindow", u"Novo projeto", None))
        self.btn_abrir_projeto.setText(QCoreApplication.translate("MainWindow", u"Abrir projeto", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Arquivos importados:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dados originais:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dados corrigidos:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v0.01", None))
    # retranslateUi

