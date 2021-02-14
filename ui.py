import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class CalculatorWindow(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Calculator")
        self.resize(800, 600)


class MainWindow(QDialog):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.button = QPushButton("Open calculator")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.button_handler)
        self.setWindowTitle("Main window")
        self.calculator_win = CalculatorWindow(self)

    def button_handler(self):
        self.calculator_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())