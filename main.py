import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(10):
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            a = randint(1, 500)
            qp.drawEllipse(10, 10, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())