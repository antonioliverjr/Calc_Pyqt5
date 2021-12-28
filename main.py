import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtCore import QObject, QEvent, Qt
import math


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora Python Qt5')
        self.setFixedSize(500, 500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: black;'
            '   color: white;'
            '   font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1
            , lambda: self.display.setText('')
            , 'background: red; '
              'color: white; '
              'font-family: serif; '
              'font-size: 25px;'
              'border-radius: 8px;'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1
            , lambda: self.display.setText(
                self.display.text()[:-1]
            )
            , 'background: blue; '
              'color: white; '
              'font-family: serif; '
              'font-size: 25px;'
              'border-radius: 8px;'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton('^'), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 2, 1, 1
            , self.eval_iqual
            , 'background: green; '
              'color: white; '
              'font-family: serif; '
              'font-size: 25px;'
              'border-radius: 8px;'
        )
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('Rz'), 4, 4, 1, 1
            , self.raiz_quadrada
        )

        #tecla.installEventFilter(self)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None
                , style='background: black; color: white; border-radius: 8px;'):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.add_text(btn)
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def add_text(self, btn):
        if 'Conta Inválida.' in self.display.text():
            return btn.text()
        else:
            return self.display.text() + btn.text()

    def eval_iqual(self):
        try:
            self.display.setText(
                str(eval(self.display.text().replace('^', '**')))
            )
        except Exception as error:
            self.display.setText('Conta Inválida.')

    def raiz_quadrada(self):
        operadores = ['+', '-', '*', '/', '^']
        for operador in operadores:
            if operador in self.display.text():
                self.display.setText('Informe apenas um número')
        else:
            try:
                self.display.setText(
                    str(round(math.sqrt(float(self.display.text())), 2))
                )
            except Exception as error:
                self.display.setText('Conta Inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
