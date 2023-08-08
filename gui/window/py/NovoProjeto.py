from qt_core import *
from gui.resources.resources_jn_novo_projeto import *

class Ui_JanelaNovoProjeto(object):
    def setupUi(self, JanelaNovoProjeto):
        if not JanelaNovoProjeto.objectName():
            JanelaNovoProjeto.setObjectName(u"JanelaNovoProjeto")
        JanelaNovoProjeto.resize(560, 250)
        JanelaNovoProjeto.setMinimumSize(QSize(560, 250))
        JanelaNovoProjeto.setMaximumSize(QSize(560, 250))
        JanelaNovoProjeto.setStyleSheet(u"*{\n"
"	font-family: \"Segoe UI\";\n"
"	color:#EFE3FE;\n"
"	\n"
"}\n"
"\n"
"#widgetNovoProjeto{\n"
"	background-color: #0F1526;\n"
"}\n"
"\n"
"#frameNovoProjeto{\n"
"	background-color: #1D2840;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#169EF2;\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #2177AD ;\n"
"	color: white;\n"
"}\n"
"\n"
"#label_local_projeto{\n"
"	background-color: #1D2840;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_nome_do_projeto{\n"
"	background-color: #1D2840;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(JanelaNovoProjeto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetNovoProjeto = QWidget(self.centralwidget)
        self.widgetNovoProjeto.setObjectName(u"widgetNovoProjeto")
        self.verticalLayout_2 = QVBoxLayout(self.widgetNovoProjeto)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameNovoProjeto = QFrame(self.widgetNovoProjeto)
        self.frameNovoProjeto.setObjectName(u"frameNovoProjeto")
        self.frameNovoProjeto.setMinimumSize(QSize(0, 25))
        self.frameNovoProjeto.setMaximumSize(QSize(16777215, 25))
        self.frameNovoProjeto.setStyleSheet(u"")
        self.frameNovoProjeto.setFrameShape(QFrame.StyledPanel)
        self.frameNovoProjeto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameNovoProjeto)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameNovoProjeto)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frameNovoProjeto)

        self.widgetNovoProjeto_2 = QWidget(self.widgetNovoProjeto)
        self.widgetNovoProjeto_2.setObjectName(u"widgetNovoProjeto_2")
        self.verticalLayout_3 = QVBoxLayout(self.widgetNovoProjeto_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.widgetNovoProjeto_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_local_projeto = QLabel(self.frame)
        self.label_local_projeto.setObjectName(u"label_local_projeto")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_local_projeto.sizePolicy().hasHeightForWidth())
        self.label_local_projeto.setSizePolicy(sizePolicy)
        self.label_local_projeto.setMinimumSize(QSize(450, 25))
        self.label_local_projeto.setMaximumSize(QSize(450, 25))
        self.label_local_projeto.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_local_projeto)

        self.btn_escolher_local_projeto = QPushButton(self.frame)
        self.btn_escolher_local_projeto.setObjectName(u"btn_escolher_local_projeto")
        self.btn_escolher_local_projeto.setMinimumSize(QSize(25, 25))
        self.btn_escolher_local_projeto.setMaximumSize(QSize(25, 25))
        self.btn_escolher_local_projeto.setStyleSheet(u"background-image: url(:/icons/cil-folder.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.horizontalLayout_2.addWidget(self.btn_escolher_local_projeto)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.widgetNovoProjeto_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 31, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_nome_do_projeto = QLineEdit(self.frame_2)
        self.lineEdit_nome_do_projeto.setObjectName(u"lineEdit_nome_do_projeto")
        self.lineEdit_nome_do_projeto.setMinimumSize(QSize(450, 25))
        self.lineEdit_nome_do_projeto.setMaximumSize(QSize(450, 25))
        self.lineEdit_nome_do_projeto.setStyleSheet(u"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.lineEdit_nome_do_projeto)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.btn_criar_projeto = QPushButton(self.widgetNovoProjeto_2)
        self.btn_criar_projeto.setObjectName(u"btn_criar_projeto")
        self.btn_criar_projeto.setMinimumSize(QSize(100, 30))
        self.btn_criar_projeto.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.btn_criar_projeto.setFont(font)

        self.verticalLayout_3.addWidget(self.btn_criar_projeto, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.widgetNovoProjeto_2)


        self.verticalLayout.addWidget(self.widgetNovoProjeto)

        JanelaNovoProjeto.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaNovoProjeto)

        QMetaObject.connectSlotsByName(JanelaNovoProjeto)
    # setupUi

    def retranslateUi(self, JanelaNovoProjeto):
        JanelaNovoProjeto.setWindowTitle(QCoreApplication.translate("JanelaNovoProjeto", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("JanelaNovoProjeto", u"<html><head/><body><p><span style=\" font-size:12pt;\">Novo Projeto</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("JanelaNovoProjeto", u"<html><head/><body><p><span style=\" font-size:12pt;\">Local:</span></p></body></html>", None))
        self.label_local_projeto.setText("")
        self.btn_escolher_local_projeto.setText("")
        self.label_3.setText(QCoreApplication.translate("JanelaNovoProjeto", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>", None))
        self.lineEdit_nome_do_projeto.setText("")
        self.btn_criar_projeto.setText(QCoreApplication.translate("JanelaNovoProjeto", u"Criar projeto", None))
    # retranslateUi

