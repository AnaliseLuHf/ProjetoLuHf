from qt_core import *
from gui.resources_dialogs import *
class Ui_DialogInfo(object):
    def setupUi(self, DialogInfo):
        if not DialogInfo.objectName():
            DialogInfo.setObjectName(u"DialogInfo")
        DialogInfo.resize(400, 200)
        DialogInfo.setMinimumSize(QSize(400, 200))
        DialogInfo.setMaximumSize(QSize(400, 200))
        DialogInfo.setStyleSheet(u"*{\n"
"	font-family:\"ArialI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"	color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"#header_content{\n"
"	background-color:rgb(33, 37, 43);\n"
"	border-bottom: 1px solid rgba(0,0,0,0.2);\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"#body_content{\n"
"	background-color:rgb(40, 44, 52);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#label_local_projeto{\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding"
                        "-left: 10px;\n"
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
        self.verticalLayout = QVBoxLayout(DialogInfo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_content = QFrame(DialogInfo)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 30))
        self.header_content.setMaximumSize(QSize(16777215, 30))
        self.header_content.setStyleSheet(u"")
        self.header_content.setFrameShape(QFrame.StyledPanel)
        self.header_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 4, 0)
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
        font1 = QFont()
        font1.setFamilies([u"ArialI"])
        font1.setPointSize(10)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.header_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(20, 20))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_fechar = QPushButton(self.frame)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(20, 20))
        self.btn_fechar.setMaximumSize(QSize(20, 20))
        self.btn_fechar.setStyleSheet(u"background-image: url(:/icones/icons/icon_close.png);")

        self.horizontalLayout_4.addWidget(self.btn_fechar)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.header_content)

        self.body_content = QFrame(DialogInfo)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.body_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_tipo_mensagem = QLabel(self.frame_4)
        self.label_tipo_mensagem.setObjectName(u"label_tipo_mensagem")
        font2 = QFont()
        font2.setFamilies([u"ArialI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_tipo_mensagem.setFont(font2)
        self.label_tipo_mensagem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_tipo_mensagem)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.body_content)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.frame_imagem = QFrame(self.frame_6)
        self.frame_imagem.setObjectName(u"frame_imagem")
        self.frame_imagem.setMinimumSize(QSize(40, 40))
        self.frame_imagem.setMaximumSize(QSize(40, 40))
        self.frame_imagem.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-image: url(:/imagens/images/icones_dialogs/info40.png);\n"
"background-position: center;")
        self.frame_imagem.setFrameShape(QFrame.StyledPanel)
        self.frame_imagem.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_imagem)

        self.label_mensagem = QLabel(self.frame_6)
        self.label_mensagem.setObjectName(u"label_mensagem")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mensagem.sizePolicy().hasHeightForWidth())
        self.label_mensagem.setSizePolicy(sizePolicy)
        self.label_mensagem.setFont(font)
        self.label_mensagem.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_mensagem.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_mensagem)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.body_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 6)
        self.btn_ok = QPushButton(self.frame_5)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(100, 30))
        self.btn_ok.setMaximumSize(QSize(100, 30))
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.btn_ok, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.body_content)


        self.retranslateUi(DialogInfo)

        QMetaObject.connectSlotsByName(DialogInfo)
    # setupUi

    def retranslateUi(self, DialogInfo):
        DialogInfo.setWindowTitle(QCoreApplication.translate("DialogInfo", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogInfo", u"Lu&Hf Data Analysis", None))
        self.btn_fechar.setText("")
        self.label_tipo_mensagem.setText(QCoreApplication.translate("DialogInfo", u"Info!", None))
        self.label_mensagem.setText(QCoreApplication.translate("DialogInfo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogInfo", u"Ok", None))
    # retranslateUi

