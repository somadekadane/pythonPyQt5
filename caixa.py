import sys
# importar os componentes para a
# construção da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout

# Construção da classe janela com o nome da caixa 
class Caixa(QWidget):
    # Criação do método _init_ que inicia a janela
    # e exibe ela em tela
    def __init__(self):
        super().__init__()

        # Vamos definir a posição e o tamanho da
        # tela
        self.setGeometry(0,30,1440,900)

        # Vamos defenir o título da nossa janela
        self.setWindowTitle("Caixa da Loja")

        # Vamos criar as labels que representam
        # as colunas esquerda e direita

        # Label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#ff5733}")

        # Label da esquerda
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#00A36C}")

        #Criar o layout horizontal para
        # as colunas
        self.h_layout = QHBoxLayout()

        # Vamos adicionar as colunas
        # esquerda e direita as layout
        # horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # Adicionar o layout na tela
        self.setLayout(self.h_layout)


app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()