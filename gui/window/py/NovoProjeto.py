from qt_core import *
from gui.resources_janela_novo_projeto import *
class Ui_JanelaNovoProjeto(object):
    def setupUi(self, JanelaNovoProjeto):
        if not JanelaNovoProjeto.objectName():
            JanelaNovoProjeto.setObjectName(u"JanelaNovoProjeto")
        JanelaNovoProjeto.resize(500, 250)
        JanelaNovoProjeto.setMinimumSize(QSize(500, 250))
        JanelaNovoProjeto.setMaximumSize(QSize(500, 250))
        JanelaNovoProjeto.setStyleSheet(u"*{\n"
"	font-family:\"ArialI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"	color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"#container_app{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#header_content{\n"
"	background-color: rgb(11, 13, 15);\n"
"	\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: red;\n"
"}\n"
"#body_content{\n"
"	background-color:rgb(26, 29, 34);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(11, 13, 15);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color:  #55afcf;\n"
"}\n"
"#label_local_projeto{\n"
"	background-color: rgb(11, 13, 15);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
""
                        "	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.centralwidget = QWidget(JanelaNovoProjeto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container_app = QFrame(self.centralwidget)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setFrameShape(QFrame.StyledPanel)
        self.container_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.container_app)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_content = QFrame(self.container_app)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 30))
        self.header_content.setMaximumSize(QSize(16777215, 30))
        self.header_content.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")
        self.header_content.setFrameShape(QFrame.StyledPanel)
        self.header_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.header_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(30, 30))
        self.frame_3.setMaximumSize(QSize(30, 30))
        self.frame_3.setStyleSheet(u"background-image:url(:/imagens/images/icon.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.header_content)
        self.frame_2.setObjectName(u"frame_2")
        font = QFont()
        font.setFamilies([u"ArialI"])
        font.setPointSize(11)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(25, 25))
        self.frame.setMaximumSize(QSize(25, 25))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_fechar_janela = QPushButton(self.frame)
        self.btn_fechar_janela.setObjectName(u"btn_fechar_janela")
        self.btn_fechar_janela.setMinimumSize(QSize(25, 25))
        self.btn_fechar_janela.setMaximumSize(QSize(25, 25))
        self.btn_fechar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_close.png);")

        self.horizontalLayout_4.addWidget(self.btn_fechar_janela)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.header_content)

        self.body_content = QFrame(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_nome = QFrame(self.body_content)
        self.frame_nome.setObjectName(u"frame_nome")
        self.frame_nome.setMinimumSize(QSize(0, 40))
        self.frame_nome.setMaximumSize(QSize(16777215, 40))
        self.frame_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nome)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.frame_nome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setFamilies([u"ArialI"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.lineEdit_nome_do_projeto = QLineEdit(self.frame_nome)
        self.lineEdit_nome_do_projeto.setObjectName(u"lineEdit_nome_do_projeto")

        self.horizontalLayout_2.addWidget(self.lineEdit_nome_do_projeto)


        self.verticalLayout_3.addWidget(self.frame_nome)

        self.frame_local_projeto = QFrame(self.body_content)
        self.frame_local_projeto.setObjectName(u"frame_local_projeto")
        self.frame_local_projeto.setMinimumSize(QSize(0, 40))
        self.frame_local_projeto.setMaximumSize(QSize(16777215, 40))
        self.frame_local_projeto.setFrameShape(QFrame.StyledPanel)
        self.frame_local_projeto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_local_projeto)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_local_projeto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_local_projeto = QLabel(self.frame_local_projeto)
        self.label_local_projeto.setObjectName(u"label_local_projeto")
        self.label_local_projeto.setMinimumSize(QSize(0, 20))
        self.label_local_projeto.setMaximumSize(QSize(16777215, 20))
        self.label_local_projeto.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_local_projeto)

        self.btn_escolher_local_projeto = QPushButton(self.frame_local_projeto)
        self.btn_escolher_local_projeto.setObjectName(u"btn_escolher_local_projeto")
        self.btn_escolher_local_projeto.setMinimumSize(QSize(80, 20))
        self.btn_escolher_local_projeto.setMaximumSize(QSize(90, 20))
        font2 = QFont()
        font2.setFamilies([u"ArialI"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.btn_escolher_local_projeto.setFont(font2)
        self.btn_escolher_local_projeto.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	background-position: left;\n"
"	font-size: 10pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid, rgba(0,0,0,0.1);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icones/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_escolher_local_projeto.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_escolher_local_projeto)


        self.verticalLayout_3.addWidget(self.frame_local_projeto)

        self.frame_5 = QFrame(self.body_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_criar_projeto = QPushButton(self.frame_5)
        self.btn_criar_projeto.setObjectName(u"btn_criar_projeto")
        self.btn_criar_projeto.setMinimumSize(QSize(100, 30))
        self.btn_criar_projeto.setMaximumSize(QSize(100, 30))
        self.btn_criar_projeto.setStyleSheet(u"QPushButton{\n"
"	background-color:  #55afcf;\n"
"	background-repeat: none;\n"
"	background-position:center;\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	font-size: 10pt;\n"
"	font-weight: bold;\n"
"	color:white ;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid, rgba(0,0,0,0.1);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_criar_projeto, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)

        JanelaNovoProjeto.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaNovoProjeto)

        QMetaObject.connectSlotsByName(JanelaNovoProjeto)
    # setupUi

    def retranslateUi(self, JanelaNovoProjeto):
        JanelaNovoProjeto.setWindowTitle(QCoreApplication.translate("JanelaNovoProjeto", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Novo Projeto", None))
        self.btn_fechar_janela.setText("")
        self.label_2.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Salvar em:", None))
        self.label_local_projeto.setText("")
        self.btn_escolher_local_projeto.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Abrir local", None))
        self.btn_criar_projeto.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Criar projeto", None))
    # retranslateUi

