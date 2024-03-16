from qt_core import *
from gui.resources import *

class Ui_BackgroundWindow(object):
    def setupUi(self, BackgroundWindow):
        if not BackgroundWindow.objectName():
            BackgroundWindow.setObjectName(u"BackgroundWindow")
        BackgroundWindow.resize(800, 500)
        BackgroundWindow.setMinimumSize(QSize(800, 500))
        BackgroundWindow.setMaximumSize(QSize(16777215, 16777215))
        BackgroundWindow.setStyleSheet(u"/*	Propriedades globais, que se aplicam em toda interface*/\n"
"*{\n"
"	font-family:\"Arial\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#container_app{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-radius: 4px;\n"
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
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #169EF2 ;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Propr"
                        "iedades que se aplicam ao menu esquerdo*/\n"
"#leftMenuContent{\n"
"	background-color: rgb(33, 37, 43);\n"
"	\n"
"}\n"
"/*	Propriedades que se aplicam ao widget do conte\u00fado principal da janela*/\n"
"#Graph_content{\n"
"	background-color:rgb(40, 44, 52);\n"
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
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles"
                        " s\u00e3o pressionados */\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-r"
                        "ight-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icones/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: grey;	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(BackgroundWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_app = QWidget(self.centralwidget)
        self.container_app.setObjectName(u"container_app")
        self.verticalLayout_2 = QVBoxLayout(self.container_app)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.btn_minimizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_minimize.png);\n"
"background-image: url(:/icones/icons/icon_minimize.png);")

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


        self.verticalLayout_2.addWidget(self.header_content)

        self.body_content = QWidget(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.body_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Graph_content = QWidget(self.body_content)
        self.Graph_content.setObjectName(u"Graph_content")
        self.Graph_content.setStyleSheet(u"border-bottom-right-radius: 4px;")
        self.verticalLayout_6 = QVBoxLayout(self.Graph_content)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.graphic_area = QWidget(self.Graph_content)
        self.graphic_area.setObjectName(u"graphic_area")
        self.verticalLayout_7 = QVBoxLayout(self.graphic_area)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_6.addWidget(self.graphic_area)

        self.grid_resize = QFrame(self.Graph_content)
        self.grid_resize.setObjectName(u"grid_resize")
        self.grid_resize.setMinimumSize(QSize(20, 20))
        self.grid_resize.setMaximumSize(QSize(20, 20))
        self.grid_resize.setStyleSheet(u"background-image: url(:/icones/icons/cil-size-grip.png);\n"
"background-repeat: none;")
        self.grid_resize.setFrameShape(QFrame.StyledPanel)
        self.grid_resize.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.grid_resize, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.Graph_content)


        self.verticalLayout_2.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)

        BackgroundWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BackgroundWindow)

        QMetaObject.connectSlotsByName(BackgroundWindow)
    # setupUi

    def retranslateUi(self, BackgroundWindow):
        BackgroundWindow.setWindowTitle(QCoreApplication.translate("BackgroundWindow", u"MainWindow", None))
        self.label_titulo_programa.setText(QCoreApplication.translate("BackgroundWindow", u"Lu&Hf An\u00e1lise de Dados - Definir Background/Sinal", None))
        self.label_nome_do_projeto.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimizar_janela.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimizar_janela.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximizar_janela.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximizar_janela.setText("")
#if QT_CONFIG(tooltip)
        self.btn_fechar_janela.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fechar_janela.setText("")
    # retranslateUi

