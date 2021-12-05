import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import random



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.a = random.randint(0, 150)
        self.do_paint = True
        self.repaint()

    def draw_flag(self, painter):
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))

        painter.drawEllipse(40, 40, 40 + self.a, 40 + self.a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
