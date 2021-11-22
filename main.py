# pyside6-rcc resources.qrc -o resources_rc.py
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PySide6.QtUiTools import loadUiType

ui, _ = loadUiType("AVG ui.ui")


class AVGui(QMainWindow, ui):
    def __init__(self):
        super(AVGui, self).__init__()

        # Remove default title bar
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        icon = QIcon("assets/avg.svg")
        self.setWindowTitle("AVG Antivirus Free")
        self.setWindowIcon(icon)

        self.setupUi(self)

        self.closeBtn.clicked.connect(self.close_window)
        self.miniBtn.clicked.connect(self.minimize_window)
        self.sideClose.clicked.connect(self.toggle_side_bar)
        self.menuBtn.clicked.connect(self.toggle_side_bar)

        self.cardShadow(self.card1)
        self.cardShadow(self.card2)
        self.cardShadow(self.card3)
        self.cardShadow(self.card4)
        self.cardShadow(self.card5)

    def close_window(self):
        self.close()

    def minimize_window(self):
        self.showMinimized()

    def toggle_side_bar(self):
        if self.sideBar.maximumWidth() == 0:
            self.sideBar.setMaximumWidth(400)
        else:
            self.sideBar.setMaximumWidth(0)
        
    def cardShadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 200))

        cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
        widget.setGraphicsEffect(shadow)

    # Move Window with mouse
    def mousePressEvent(self, event):
        self.dragPos = self.pos()
        self.mouse_original_pos = self.mapToGlobal(event.pos())

    def mouseMoveEvent(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            if event.buttons() == Qt.LeftButton:
                last_pos = self.dragPos + self.mapToGlobal(event.pos()) - self.mouse_original_pos
                self.move(last_pos)
                event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AVGui()
    win.show()
    sys.exit(app.exec())

