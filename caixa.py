import sys
# importar os componentes para a
# construção da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

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
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#cccccc}")

        # Label da esquerda
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#808080}")
        
        # Criar o comteúdo da coluna da esquerda 
        self.v_layout_esquerda = QVBoxLayout()
        
        # Vamos criar uma label para adicionar o logo da nossa
        #loja
        self.logo_label=QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/eder.jgsilva/Documents/JanelaCaixa/.venv/cocacola20.png"))
        # Ajudar a label e a imagem para ficar do tamanho 
        # ideal
        self.logo_label.setScaledContents(True)

        self.logo_label.setFixedHeight(200)
        self.logo_label.setFixedWidth(200)

        # Adionar a label com a imagem na tela
        self.v_layout_esquerda.addWidget(self.logo_label)

        # Vamos criar as labels e as linesEdits que ficarão na coluna
        # da esquerda, dentro do layout vertical da esquerda
        self.codigo_produto_label = QLabel("Código do Produto:")
        self.codigo_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto:")
        self.nome_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Descrição do Produto:")
        self.descricao_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto:")
        self.quantidade_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)
  
        self.preco_unitario_label = QLabel("Preço Unitário do Produto:")
        self.preco_unitario_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preco_unitario_label)
        self.v_layout_esquerda.addWidget(self.preco_unitario_edit)

        self.sub_total_label = QLabel ("Sub Total:")
        self.sub_total_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.sub_total_label)
        self.v_layout_esquerda.addWidget(self.sub_total_edit)

        # adicionao o layout vertical da esquerda com
        # todos os controles:label e lineEdit dentro
        # da colona da esquerda(label_coluna_esquerda)
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)

        # ----------- Controle da coluna da direita ----------
        self.v_layout_direita = QVBoxLayout()
        # Criar um tabela e adicionar na coluna da direita
        # esta tabela terá os nome dos campos que estão
        # ao esquerda
        # Colunas da tabela
        colunas = ["Produto","Nome do produto","Descrição","Quantidade","Preço Unitário","Subtotal" ]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)

        self.total_pagar_label = QLabel("Total a Pagar")
        self.total_pagar_edit = QLineEdit("0,00")
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)

        self.label_coluna_direita.setLayout(self.v_layout_direita)



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