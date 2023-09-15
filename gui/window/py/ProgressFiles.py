from qt_core import *


class Ui_ProgressoArquivosImportados(object):
    def setupUi(self, ProgressoArquivosImportados):
        if not ProgressoArquivosImportados.objectName():
            ProgressoArquivosImportados.setObjectName(u"ProgressoArquivosImportados")
        ProgressoArquivosImportados.resize(600, 170)
        ProgressoArquivosImportados.setMinimumSize(QSize(600, 170))
        ProgressoArquivosImportados.setMaximumSize(QSize(600, 170))
        ProgressoArquivosImportados.setStyleSheet(u"*{\n"
"	font-family: \"Bahnschrift\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#splash{\n"
"	background-color:rgb(40, 44, 52);\n"
"	border-radius: 10px;\n"
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
"	\n"
"\n"
"\n"
"}")
        self.centralwidget = QWidget(ProgressoArquivosImportados)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splash = QFrame(self.centralwidget)
        self.splash.setObjectName(u"splash")
        self.splash.setMinimumSize(QSize(580, 130))
        self.splash.setMaximumSize(QSize(580, 130))
        self.splash.setFrameShape(QFrame.StyledPanel)
        self.splash.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.splash)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(202, 30, 191, 30))
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"color: grey;\n"
"font-size: 14pt;")
        self.progressBar = QProgressBar(self.splash)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 70, 500, 20))
        self.progressBar.setMinimumSize(QSize(500, 0))
        self.progressBar.setMaximumSize(QSize(500, 16777215))
        self.progressBar.setValue(24)
        self.label_num_arquivos = QLabel(self.splash)
        self.label_num_arquivos.setObjectName(u"label_num_arquivos")
        self.label_num_arquivos.setGeometry(QRect(262, 96, 61, 20))
        self.label_num_arquivos.setMinimumSize(QSize(0, 20))
        self.label_num_arquivos.setMaximumSize(QSize(16777215, 20))
        self.label_num_arquivos.setStyleSheet(u"color: grey;\n"
"font-size: 10pt;")
        self.label_num_arquivos.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.splash)

        ProgressoArquivosImportados.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgressoArquivosImportados)

        QMetaObject.connectSlotsByName(ProgressoArquivosImportados)
    # setupUi

    def retranslateUi(self, ProgressoArquivosImportados):
        ProgressoArquivosImportados.setWindowTitle(QCoreApplication.translate("ProgressoArquivosImportados", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ProgressoArquivosImportados", u"Importando arquivos...", None))
        self.label_num_arquivos.setText(QCoreApplication.translate("ProgressoArquivosImportados", u"20/100", None))
    # retranslateUi

