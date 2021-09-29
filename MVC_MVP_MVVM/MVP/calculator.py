from model import ModelCalculator
from view import ViewCalculator
from presenter import PresenterCalculator
import PyQt5.QtWidgets as QtWidgets
import sys


class Calculator(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.window = QtWidgets.QMainWindow()
        demo_view = ViewCalculator()
        demo_model = ModelCalculator()
        self.presenter = PresenterCalculator(demo_view, demo_model)
        self.setCentralWidget(demo_view)
        self.setWindowTitle('Калькулятор на MVP')


def qapp():
    if QtWidgets.QApplication.instance():
        calc_app = QtWidgets.QApplication.instance()
    else:
        calc_app = QtWidgets.QApplication(sys.argv)
    return calc_app


if __name__ == '__main__':
    app = qapp()
    window = Calculator()
    window.show()
    app.exec_()
