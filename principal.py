import sys

from proj_composting import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class Principal (Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self._init_components()
        self.cor_sucesso = 'background-color: rgb(66, 245, 170);'
        self.cor_erro = 'background-color: rgb(242, 70, 70);'

    def _init_components(self) -> None:
        #tela_login apresentação da página inicial
        self.label_login_img_pag5.setPixmap(QPixmap('img/img_logo_maior'))
        self.frame_login_msg_pag1.hide()
        self.pushButton_login_fechar_msg.clicked.connect(lambda: self.frame_login_msg_pag1.hide())
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)

        #tela cadastro
        self.label_cadastro_logo_pag2.setPixmap(QPixmap('img/img_logo_maior'))
        self.pushButton_cadastro_salvar.clicked.connect#(self.acessar_lista)
        self.pushButton_cadastro_limpar.clicked.connect#(self.sair_sistema)
        self.pushButton_cadastro_ok_pag2.clicked.connect(lambda: self.frame_msg_erro_pag2.hide())

        #tela_lista exibir a lista
        self.label_lista_logo.setPixmap(QPixmap('img/img_logo_menor'))
        self.frame_lista_msg.hide()
        self.pushButton_ok_pag3.clicked.connect(lambda: self.frame_lista_msg.hide())
        self.pushButton_excluir_pag3.clicked.connect#(self.excluir_material)
        self.pushButton_aletrar_pag3.clicked.connect#(self.alterar_material)
        self.pushButton_voltar_pag3_.clicked.connect(lambda: self.frame_cadastro_area.hide())
        self.pushButton_proximo_pag3.clicked.connect(lambda: self.frame_home_area.hide())
        self.pushButton_home_pag3.clicked.connect(self.frame_login_area_login_pag1)


    def realizar_login(self):
        nome = self.lineEdit_login_estabelecimento.text()
        endereco = self.lineEdit_login_endereco.text()
        if nome == '' and endereco == '':
            self.lineEdit_login_estabelecimento.clear()
            self.lineEdit_login_endereco.clear()
            self.frame_login_msg_pag1.hide()
            #self.acessar_home()
        else:
            self.label_login_msg_erro.setText('Não foi possível concluir o cadastro!')
            self.frame_login_msg_pag1.show()

    
        