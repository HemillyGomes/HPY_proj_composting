# Form implementation generated from reading ui file 'proj_composting.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 572)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_principal = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_principal.setGeometry(QtCore.QRect(0, 0, 831, 501))
        self.frame_principal.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.stackedWidget_paginas = QtWidgets.QStackedWidget(parent=self.frame_principal)
        self.stackedWidget_paginas.setGeometry(QtCore.QRect(30, 40, 771, 491))
        self.stackedWidget_paginas.setMinimumSize(QtCore.QSize(141, 141))
        self.stackedWidget_paginas.setObjectName("stackedWidget_paginas")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.frame_login_area_login_pag1 = QtWidgets.QFrame(parent=self.page_login)
        self.frame_login_area_login_pag1.setGeometry(QtCore.QRect(20, 20, 711, 391))
        self.frame_login_area_login_pag1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_login_area_login_pag1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login_area_login_pag1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login_area_login_pag1.setObjectName("frame_login_area_login_pag1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_login_area_login_pag1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEdit_login_estabelecimento = QtWidgets.QLineEdit(parent=self.frame_login_area_login_pag1)
        self.lineEdit_login_estabelecimento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_login_estabelecimento.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_login_estabelecimento.setObjectName("lineEdit_login_estabelecimento")
        self.gridLayout_2.addWidget(self.lineEdit_login_estabelecimento, 1, 1, 1, 1)
        self.pushButton_login_entrar = QtWidgets.QPushButton(parent=self.frame_login_area_login_pag1)
        self.pushButton_login_entrar.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_login_entrar.setObjectName("pushButton_login_entrar")
        self.gridLayout_2.addWidget(self.pushButton_login_entrar, 4, 1, 1, 1)
        self.label_login_img_pag5 = QtWidgets.QLabel(parent=self.frame_login_area_login_pag1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_login_img_pag5.sizePolicy().hasHeightForWidth())
        self.label_login_img_pag5.setSizePolicy(sizePolicy)
        self.label_login_img_pag5.setMinimumSize(QtCore.QSize(145, 145))
        self.label_login_img_pag5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_img_pag5.setObjectName("label_login_img_pag5")
        self.gridLayout_2.addWidget(self.label_login_img_pag5, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.lineEdit_login_endereco = QtWidgets.QLineEdit(parent=self.frame_login_area_login_pag1)
        self.lineEdit_login_endereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_login_endereco.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_login_endereco.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_login_endereco.setObjectName("lineEdit_login_endereco")
        self.gridLayout_2.addWidget(self.lineEdit_login_endereco, 2, 1, 1, 1)
        self.frame_login_msg_pag1 = QtWidgets.QFrame(parent=self.frame_login_area_login_pag1)
        self.frame_login_msg_pag1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login_msg_pag1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login_msg_pag1.setObjectName("frame_login_msg_pag1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_login_msg_pag1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_login_msg_erro = QtWidgets.QLabel(parent=self.frame_login_msg_pag1)
        self.label_login_msg_erro.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label_login_msg_erro.setObjectName("label_login_msg_erro")
        self.gridLayout_3.addWidget(self.label_login_msg_erro, 0, 0, 1, 1)
        self.pushButton_login_fechar_msg = QtWidgets.QPushButton(parent=self.frame_login_msg_pag1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login_fechar_msg.sizePolicy().hasHeightForWidth())
        self.pushButton_login_fechar_msg.setSizePolicy(sizePolicy)
        self.pushButton_login_fechar_msg.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_login_fechar_msg.setObjectName("pushButton_login_fechar_msg")
        self.gridLayout_3.addWidget(self.pushButton_login_fechar_msg, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_login_msg_pag1, 3, 0, 1, 3)
        self.stackedWidget_paginas.addWidget(self.page_login)
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.frame_cadastro_area = QtWidgets.QFrame(parent=self.page_home)
        self.frame_cadastro_area.setGeometry(QtCore.QRect(10, 50, 741, 301))
        self.frame_cadastro_area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_cadastro_area.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastro_area.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastro_area.setObjectName("frame_cadastro_area")
        self.frame_cadastro_formulario = QtWidgets.QFrame(parent=self.frame_cadastro_area)
        self.frame_cadastro_formulario.setGeometry(QtCore.QRect(10, 140, 571, 88))
        self.frame_cadastro_formulario.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastro_formulario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastro_formulario.setObjectName("frame_cadastro_formulario")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_cadastro_formulario)
        self.gridLayout.setObjectName("gridLayout")
        self.label_cadastro_quantidade = QtWidgets.QLabel(parent=self.frame_cadastro_formulario)
        self.label_cadastro_quantidade.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_cadastro_quantidade.setObjectName("label_cadastro_quantidade")
        self.gridLayout.addWidget(self.label_cadastro_quantidade, 1, 0, 1, 1)
        self.label_cadastro_fornecedor = QtWidgets.QLabel(parent=self.frame_cadastro_formulario)
        self.label_cadastro_fornecedor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_cadastro_fornecedor.setObjectName("label_cadastro_fornecedor")
        self.gridLayout.addWidget(self.label_cadastro_fornecedor, 0, 0, 1, 1)
        self.comboBox_cadastro_quantidade = QtWidgets.QComboBox(parent=self.frame_cadastro_formulario)
        self.comboBox_cadastro_quantidade.setObjectName("comboBox_cadastro_quantidade")
        self.comboBox_cadastro_quantidade.addItem("")
        self.comboBox_cadastro_quantidade.addItem("")
        self.comboBox_cadastro_quantidade.addItem("")
        self.comboBox_cadastro_quantidade.addItem("")
        self.comboBox_cadastro_quantidade.addItem("")
        self.gridLayout.addWidget(self.comboBox_cadastro_quantidade, 1, 1, 1, 1)
        self.lineEdit_cadastro_fornecedor = QtWidgets.QLineEdit(parent=self.frame_cadastro_formulario)
        self.lineEdit_cadastro_fornecedor.setObjectName("lineEdit_cadastro_fornecedor")
        self.gridLayout.addWidget(self.lineEdit_cadastro_fornecedor, 0, 1, 1, 1)
        self.frame_msg_erro_pag2 = QtWidgets.QFrame(parent=self.frame_cadastro_area)
        self.frame_msg_erro_pag2.setGeometry(QtCore.QRect(130, 10, 581, 71))
        self.frame_msg_erro_pag2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_erro_pag2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_erro_pag2.setObjectName("frame_msg_erro_pag2")
        self.label_cadastro_msg_erro_pag2 = QtWidgets.QLabel(parent=self.frame_msg_erro_pag2)
        self.label_cadastro_msg_erro_pag2.setGeometry(QtCore.QRect(10, 40, 351, 21))
        self.label_cadastro_msg_erro_pag2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label_cadastro_msg_erro_pag2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_msg_erro_pag2.setObjectName("label_cadastro_msg_erro_pag2")
        self.pushButton_cadastro_ok_pag2 = QtWidgets.QPushButton(parent=self.frame_msg_erro_pag2)
        self.pushButton_cadastro_ok_pag2.setGeometry(QtCore.QRect(490, 40, 75, 23))
        self.pushButton_cadastro_ok_pag2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_cadastro_ok_pag2.setObjectName("pushButton_cadastro_ok_pag2")
        self.label_cadastro_logo_pag2 = QtWidgets.QLabel(parent=self.frame_cadastro_area)
        self.label_cadastro_logo_pag2.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.label_cadastro_logo_pag2.setStyleSheet("")
        self.label_cadastro_logo_pag2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_logo_pag2.setObjectName("label_cadastro_logo_pag2")
        self.frame_cadastro_botoes = QtWidgets.QFrame(parent=self.frame_cadastro_area)
        self.frame_cadastro_botoes.setGeometry(QtCore.QRect(600, 140, 121, 91))
        self.frame_cadastro_botoes.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_cadastro_botoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastro_botoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastro_botoes.setObjectName("frame_cadastro_botoes")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_cadastro_botoes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_cadastro_salvar = QtWidgets.QPushButton(parent=self.frame_cadastro_botoes)
        self.pushButton_cadastro_salvar.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_cadastro_salvar.setObjectName("pushButton_cadastro_salvar")
        self.verticalLayout.addWidget(self.pushButton_cadastro_salvar)
        self.pushButton_cadastro_limpar = QtWidgets.QPushButton(parent=self.frame_cadastro_botoes)
        self.pushButton_cadastro_limpar.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_cadastro_limpar.setObjectName("pushButton_cadastro_limpar")
        self.verticalLayout.addWidget(self.pushButton_cadastro_limpar)
        self.stackedWidget_paginas.addWidget(self.page_home)
        self.page_cadastro = QtWidgets.QWidget()
        self.page_cadastro.setObjectName("page_cadastro")
        self.frame_lista_mat_org_pag3 = QtWidgets.QFrame(parent=self.page_cadastro)
        self.frame_lista_mat_org_pag3.setGeometry(QtCore.QRect(30, 20, 751, 451))
        self.frame_lista_mat_org_pag3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_lista_mat_org_pag3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_lista_mat_org_pag3.setObjectName("frame_lista_mat_org_pag3")
        self.tableWidget_fornecedor_pag3 = QtWidgets.QTableWidget(parent=self.frame_lista_mat_org_pag3)
        self.tableWidget_fornecedor_pag3.setGeometry(QtCore.QRect(120, 120, 401, 311))
        self.tableWidget_fornecedor_pag3.setObjectName("tableWidget_fornecedor_pag3")
        self.tableWidget_fornecedor_pag3.setColumnCount(4)
        self.tableWidget_fornecedor_pag3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_fornecedor_pag3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_fornecedor_pag3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_fornecedor_pag3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_fornecedor_pag3.setHorizontalHeaderItem(3, item)
        self.frame_lista_botoes_pag3 = QtWidgets.QFrame(parent=self.frame_lista_mat_org_pag3)
        self.frame_lista_botoes_pag3.setGeometry(QtCore.QRect(590, 120, 101, 351))
        self.frame_lista_botoes_pag3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 255, 255);\n"
"}")
        self.frame_lista_botoes_pag3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_lista_botoes_pag3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_lista_botoes_pag3.setObjectName("frame_lista_botoes_pag3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_lista_botoes_pag3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_excluir_pag3 = QtWidgets.QPushButton(parent=self.frame_lista_botoes_pag3)
        self.pushButton_excluir_pag3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_excluir_pag3.setObjectName("pushButton_excluir_pag3")
        self.verticalLayout_2.addWidget(self.pushButton_excluir_pag3)
        self.pushButton_aletrar_pag3 = QtWidgets.QPushButton(parent=self.frame_lista_botoes_pag3)
        self.pushButton_aletrar_pag3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_aletrar_pag3.setObjectName("pushButton_aletrar_pag3")
        self.verticalLayout_2.addWidget(self.pushButton_aletrar_pag3)
        self.pushButton_voltar_pag3_ = QtWidgets.QPushButton(parent=self.frame_lista_botoes_pag3)
        self.pushButton_voltar_pag3_.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_voltar_pag3_.setObjectName("pushButton_voltar_pag3_")
        self.verticalLayout_2.addWidget(self.pushButton_voltar_pag3_)
        self.pushButton_proximo_pag3 = QtWidgets.QPushButton(parent=self.frame_lista_botoes_pag3)
        self.pushButton_proximo_pag3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_proximo_pag3.setObjectName("pushButton_proximo_pag3")
        self.verticalLayout_2.addWidget(self.pushButton_proximo_pag3)
        self.pushButton_home_pag3 = QtWidgets.QPushButton(parent=self.frame_lista_botoes_pag3)
        self.pushButton_home_pag3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_home_pag3.setObjectName("pushButton_home_pag3")
        self.verticalLayout_2.addWidget(self.pushButton_home_pag3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_lista_logo = QtWidgets.QLabel(parent=self.frame_lista_mat_org_pag3)
        self.label_lista_logo.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.label_lista_logo.setStyleSheet("")
        self.label_lista_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_lista_logo.setObjectName("label_lista_logo")
        self.frame_lista_msg = QtWidgets.QFrame(parent=self.frame_lista_mat_org_pag3)
        self.frame_lista_msg.setGeometry(QtCore.QRect(120, 10, 571, 101))
        self.frame_lista_msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_lista_msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_lista_msg.setObjectName("frame_lista_msg")
        self.label_msg_erro_pag3 = QtWidgets.QLabel(parent=self.frame_lista_msg)
        self.label_msg_erro_pag3.setGeometry(QtCore.QRect(10, 40, 391, 21))
        self.label_msg_erro_pag3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label_msg_erro_pag3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_msg_erro_pag3.setObjectName("label_msg_erro_pag3")
        self.pushButton_ok_pag3 = QtWidgets.QPushButton(parent=self.frame_lista_msg)
        self.pushButton_ok_pag3.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.pushButton_ok_pag3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_ok_pag3.setObjectName("pushButton_ok_pag3")
        self.stackedWidget_paginas.addWidget(self.page_cadastro)
        self.page_fim = QtWidgets.QWidget()
        self.page_fim.setObjectName("page_fim")
        self.frame_home_area = QtWidgets.QFrame(parent=self.page_fim)
        self.frame_home_area.setGeometry(QtCore.QRect(30, 40, 721, 411))
        self.frame_home_area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_home_area.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_home_area.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_home_area.setObjectName("frame_home_area")
        self.frame_home_logo_pag5 = QtWidgets.QFrame(parent=self.frame_home_area)
        self.frame_home_logo_pag5.setGeometry(QtCore.QRect(10, 20, 671, 161))
        self.frame_home_logo_pag5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_home_logo_pag5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_home_logo_pag5.setObjectName("frame_home_logo_pag5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_home_logo_pag5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_home_logo_pag5 = QtWidgets.QLabel(parent=self.frame_home_logo_pag5)
        self.label_home_logo_pag5.setMinimumSize(QtCore.QSize(145, 145))
        self.label_home_logo_pag5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_home_logo_pag5.setObjectName("label_home_logo_pag5")
        self.gridLayout_5.addWidget(self.label_home_logo_pag5, 0, 1, 1, 1)
        self.frame_saida_botoes_pag5 = QtWidgets.QFrame(parent=self.frame_home_area)
        self.frame_saida_botoes_pag5.setGeometry(QtCore.QRect(200, 230, 291, 81))
        self.frame_saida_botoes_pag5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_saida_botoes_pag5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_saida_botoes_pag5.setObjectName("frame_saida_botoes_pag5")
        self.pushButton_novo_pag5 = QtWidgets.QPushButton(parent=self.frame_saida_botoes_pag5)
        self.pushButton_novo_pag5.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.pushButton_novo_pag5.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_novo_pag5.setObjectName("pushButton_novo_pag5")
        self.pushButton_sair_pag5 = QtWidgets.QPushButton(parent=self.frame_saida_botoes_pag5)
        self.pushButton_sair_pag5.setGeometry(QtCore.QRect(200, 30, 81, 21))
        self.pushButton_sair_pag5.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton_sair_pag5.setObjectName("pushButton_sair_pag5")
        self.stackedWidget_paginas.addWidget(self.page_fim)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_paginas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_login_estabelecimento.setPlaceholderText(_translate("MainWindow", "Insira o nome do estabelecimento"))
        self.pushButton_login_entrar.setText(_translate("MainWindow", "Entrar"))
        self.label_login_img_pag5.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_login_endereco.setPlaceholderText(_translate("MainWindow", "Insira o endereço"))
        self.label_login_msg_erro.setText(_translate("MainWindow", "                Não foi possível concluir o cadastro!"))
        self.pushButton_login_fechar_msg.setText(_translate("MainWindow", "ok"))
        self.label_cadastro_quantidade.setText(_translate("MainWindow", "Quantidade (kg):"))
        self.label_cadastro_fornecedor.setText(_translate("MainWindow", "Fornecedor:"))
        self.comboBox_cadastro_quantidade.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_cadastro_quantidade.setItemText(1, _translate("MainWindow", "20 "))
        self.comboBox_cadastro_quantidade.setItemText(2, _translate("MainWindow", "30 "))
        self.comboBox_cadastro_quantidade.setItemText(3, _translate("MainWindow", "40"))
        self.comboBox_cadastro_quantidade.setItemText(4, _translate("MainWindow", "50"))
        self.label_cadastro_msg_erro_pag2.setText(_translate("MainWindow", "Erro!"))
        self.pushButton_cadastro_ok_pag2.setText(_translate("MainWindow", "Ok"))
        self.label_cadastro_logo_pag2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_cadastro_salvar.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_cadastro_limpar.setText(_translate("MainWindow", "Limpar"))
        item = self.tableWidget_fornecedor_pag3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fornecedor "))
        item = self.tableWidget_fornecedor_pag3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantidade(kg)"))
        item = self.tableWidget_fornecedor_pag3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dia da Semana"))
        item = self.tableWidget_fornecedor_pag3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Húmus (kg)"))
        self.pushButton_excluir_pag3.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_aletrar_pag3.setText(_translate("MainWindow", "Alterar"))
        self.pushButton_voltar_pag3_.setText(_translate("MainWindow", "Voltar"))
        self.pushButton_proximo_pag3.setText(_translate("MainWindow", "Próximo"))
        self.pushButton_home_pag3.setText(_translate("MainWindow", "Home"))
        self.label_lista_logo.setText(_translate("MainWindow", "TextLabel"))
        self.label_msg_erro_pag3.setText(_translate("MainWindow", "Erro!"))
        self.pushButton_ok_pag3.setText(_translate("MainWindow", "Ok"))
        self.label_home_logo_pag5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_novo_pag5.setText(_translate("MainWindow", "Novo"))
        self.pushButton_sair_pag5.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
