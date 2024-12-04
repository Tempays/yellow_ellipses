import io
import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(615, 500)
        self.button.clicked.connect(self.paint)
        self.paint_ = False

    def paintEvent(self, event):
        if self.paint_:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
        self.paint_ = False

    def paint(self):
        self.paint_ = True
        self.update()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        number = randint(1, 7)
        for _ in range(number):
            radius = randint(20, 500)
            qp.drawEllipse(randint(-50, 450), randint(-50, 450), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Widget()
    wnd.show()
    sys.exit(app.exec())