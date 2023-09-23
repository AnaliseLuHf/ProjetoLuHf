from qt_core import *
from gui.resources_dialogs import *
class Ui_ProgressoImportao(object):
    def setupUi(self, ProgressoImportao):
        if not ProgressoImportao.objectName():
            ProgressoImportao.setObjectName(u"ProgressoImportao")
        ProgressoImportao.resize(590, 200)
        ProgressoImportao.setMinimumSize(QSize(590, 200))
        ProgressoImportao.setMaximumSize(QSize(590, 200))
        ProgressoImportao.setStyleSheet(u"*{\n"
"	font-family: \"Bahnschrift\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"\n"
"\n"
"#header_content{\n"
"	background-color: rgb(11, 13, 15);\n"
"}	\n"
"\n"
"#body_content{\n"
"	background-color:rgb(40, 44, 52);\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ProgressBar */\n"
"\n"
"QProgressBar {\n"
"	color: black;\n"
"	text-align: center;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white , stop:0.5 #55afcf , stop:1 #085c83);\n"
"}")
        self.verticalLayout = QVBoxLayout(ProgressoImportao)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container_app = QFrame(ProgressoImportao)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setMinimumSize(QSize(580, 170))
        self.container_app.setMaximumSize(QSize(580, 170))
        self.container_app.setFrameShape(QFrame.StyledPanel)
        self.container_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.container_app)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
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
        font.setFamilies([u"Bahnschrift"])
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
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: grey;")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.header_content)

        self.body_content = QFrame(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.body_content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setStyleSheet(u"color: grey;\n"
"font-size: 14pt;")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.body_content)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(500, 20))
        self.progressBar.setMaximumSize(QSize(500, 20))
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.label_num_arquivos = QLabel(self.body_content)
        self.label_num_arquivos.setObjectName(u"label_num_arquivos")
        self.label_num_arquivos.setMinimumSize(QSize(0, 20))
        self.label_num_arquivos.setMaximumSize(QSize(16777215, 20))
        self.label_num_arquivos.setStyleSheet(u"color: grey;\n"
"font-size: 10pt;")
        self.label_num_arquivos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_num_arquivos, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)


        self.retranslateUi(ProgressoImportao)

        QMetaObject.connectSlotsByName(ProgressoImportao)
    # setupUi

    def retranslateUi(self, ProgressoImportao):
        ProgressoImportao.setWindowTitle(QCoreApplication.translate("ProgressoImportao", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ProgressoImportao", u"Lu&Hf Data Analysis", None))
        self.label_2.setText(QCoreApplication.translate("ProgressoImportao", u"Importando arquivos...", None))
        self.label_num_arquivos.setText("")
    # retranslateUi

