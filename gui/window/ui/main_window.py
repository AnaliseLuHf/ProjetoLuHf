from qt_core import *
from gui.resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 530)
        MainWindow.setStyleSheet(u"*{\n"
"	font-family:\"Bahnschrift Light\";\n"
"}\n"
"#centralwidget{\n"
"	background-color:#17181A;\n"
"	\n"
"}\n"
"#leftMenuContent{\n"
"	background-color: #202123;\n"
"}\n"
"#bodyContent{\n"
"	background-color:#17181A;\n"
"}\n"
"#header_content{\n"
"	background-color:#025939;\n"
"}\n"
"#footer_content{\n"
"	background-color:#025939;\n"
"}\n"
"\n"
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
"#frame_redm_janela QPushButton{\n"
"	background-color: transparent;\n"
"	background-position: center;\n"
"	background-repeat:none;\n"
"	border: none;\n"
"}\n"
"\n"
"#leftMenuContent QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftMenuContent .QPushButton:pressed {	\n"
"	background-color: #04BF7B;\n"
"	color: rgb(255,"
                        " 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_content = QWidget(self.centralwidget)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 35))
        self.header_content.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.header_content)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_logo)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame_logo, 0, Qt.AlignLeft)

        self.frame_nome_programa = QFrame(self.header_content)
        self.frame_nome_programa.setObjectName(u"frame_nome_programa")
        self.frame_nome_programa.setFrameShape(QFrame.StyledPanel)
        self.frame_nome_programa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_nome_programa)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_nome_programa)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Bahnschrift Light"])
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame_nome_programa)

        self.frame_redm_janela = QFrame(self.header_content)
        self.frame_redm_janela.setObjectName(u"frame_redm_janela")
        self.frame_redm_janela.setFrameShape(QFrame.StyledPanel)
        self.frame_redm_janela.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_redm_janela)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_fechar_janela = QPushButton(self.frame_redm_janela)
        self.btn_fechar_janela.setObjectName(u"btn_fechar_janela")
        self.btn_fechar_janela.setMinimumSize(QSize(28, 28))
        self.btn_fechar_janela.setMaximumSize(QSize(28, 28))
        self.btn_fechar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_minimize.png);")

        self.horizontalLayout_4.addWidget(self.btn_fechar_janela)

        self.btn_maximizar_janela = QPushButton(self.frame_redm_janela)
        self.btn_maximizar_janela.setObjectName(u"btn_maximizar_janela")
        self.btn_maximizar_janela.setMinimumSize(QSize(28, 28))
        self.btn_maximizar_janela.setMaximumSize(QSize(28, 28))
        self.btn_maximizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_maximize.png);")

        self.horizontalLayout_4.addWidget(self.btn_maximizar_janela)

        self.btn_minimizar_janela = QPushButton(self.frame_redm_janela)
        self.btn_minimizar_janela.setObjectName(u"btn_minimizar_janela")
        self.btn_minimizar_janela.setMinimumSize(QSize(28, 28))
        self.btn_minimizar_janela.setMaximumSize(QSize(28, 28))
        self.btn_minimizar_janela.setStyleSheet(u"background-image: url(:/icones/icons/icon_close.png);")

        self.horizontalLayout_4.addWidget(self.btn_minimizar_janela)


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
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_menu.setFont(font1)
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

        self.pushButton_3 = QPushButton(self.frame_center_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 45))
        self.pushButton_3.setMaximumSize(QSize(16777215, 45))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/icones/icons/cil-3d.png);")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_center_menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 45))
        self.pushButton_4.setMaximumSize(QSize(16777215, 45))
        self.pushButton_4.setStyleSheet(u"background-image: url(:/icones/icons/cil-alarm.png);")

        self.verticalLayout_4.addWidget(self.pushButton_4)

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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.footer_content = QWidget(self.mainBodyContent)
        self.footer_content.setObjectName(u"footer_content")
        self.footer_content.setMinimumSize(QSize(0, 25))
        self.footer_content.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.footer_content, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.mainBodyContent)


        self.verticalLayout.addWidget(self.app_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOME DO PROGRAMA", None))
        self.btn_fechar_janela.setText("")
        self.btn_maximizar_janela.setText("")
        self.btn_minimizar_janela.setText("")
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o 3", None))
    # retranslateUi

