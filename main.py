import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication
from random import randint
from interface import MyWidget


class Widget(MyWidget):
    def __init__(self):
        super().__init__()
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
        number = randint(1, 7)
        for _ in range(number):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            radius = randint(20, 500)
            qp.drawEllipse(randint(-50, 450), randint(-50, 450), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Widget()
    wnd.show()
    sys.exit(app.exec())