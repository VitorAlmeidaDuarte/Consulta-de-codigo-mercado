from Models.Hortfuit_schemma import ControlerHortifruit
from PyQt5 import QtWidgets, uic
import sys




class HortfruitWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(HortfruitWindow, self).__init__()
        uic.loadUi('interface.ui/HortfruitPainel.ui', self)
        self.show()
        self.codigo_do_item = []

       # self.input_fruta = self.findChild(QtWidgets.Qlabel, 'text_hortfruit') 
        

        #------- atribuido ações aos botões
        self.pushButton_0.clicked.connect(lambda: self.adicionar_numero_string(0))
        self.pushButton_1.clicked.connect(lambda: self.adicionar_numero_string(1))
        self.pushButton_2.clicked.connect(lambda: self.adicionar_numero_string(2))
        self.pushButton_3.clicked.connect(lambda: self.adicionar_numero_string(3))
        self.pushButton_4.clicked.connect(lambda: self.adicionar_numero_string(4))
        self.pushButton_5.clicked.connect(lambda: self.adicionar_numero_string(5))
        self.pushButton_6.clicked.connect(lambda: self.adicionar_numero_string(6))
        self.pushButton_7.clicked.connect(lambda: self.adicionar_numero_string(7))
        self.pushButton_8.clicked.connect(lambda: self.adicionar_numero_string(8))
        self.pushButton_9.clicked.connect(lambda: self.adicionar_numero_string(9))

        self.pushButton_Balanca.clicked.connect(self.pesquisar_frutas)
        

    def adicionar_numero_string(self, numero):
        self.codigo_do_item.append(numero)
    
    def pesquisar_frutas(self):
        codigo = ''
        for numero in self.codigo_do_item:
            codigo += str(numero)
        fruta_objeto = ControlerHortifruit.procurar_fruta_por_codigo(codigo)

        self.text_hortfruit.setText(fruta_objeto.nome)


        #TODO. arrumar o text_hortfruit deixar bonito, fazer a fruta aparacer no painel, zerar lista quando apertar em ENTRA

app = QtWidgets.QApplication(sys.argv)
window = HortfruitWindow()
app.exec_()        