import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets


class ViewCalculator(QtWidgets.QDialog):
    displaySignal = QtCore.pyqtSignal()
    btnSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ViewCalculator, self).__init__(parent)

        self.table = QtWidgets.QTableWidget()
        self.table.setWindowTitle('Калькулятор на MVP')
        self.table.resize(600, 600)
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels('Имя;Значение;'.split(';'))

        keys = ['Значение 1', 'Операция', 'Значение 2', 'Выбор дисплея', 'Результат']
        self.combo = {}
        self.create_combo_table(1, 1, 'operations')
        self.create_combo_table(3, 1, 'display')
        for row in range(len(keys)):
            self.set_names(keys[row], row)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.table)

        self.button = QtWidgets.QPushButton('Рассчёт', self)
        self.button.setStyleSheet('background-color:lightgrey')
        grid.addWidget(self.button)

        self.button.clicked.connect(self.btn_click)
        self.combo['display'].currentIndexChanged.connect(self.display_changed)

        self.setLayout(grid)

    def btn_click(self):
        self.btnSignal.emit()

    def display_changed(self):
        self.displaySignal.emit()

    def create_combo_table(self, row, col, key):
        self.combo[key] = QtWidgets.QComboBox()
        options = ['test']
        self.combo[key].addItems(options)
        self.table.setCellWidget(row, col, self.combo[key])

    def set_options(self, key, options):
        self.combo[key].clear()
        self.combo[key].addItems(options)

    def set_names(self, name, row):
        text = QtWidgets.QTableWidgetItem(name)
        text.setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(row, 0, text)

    def setResult(self, value):
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem(str(value)))

    def hide_display(self):
        self.table.setRowHidden(4, True)

    def show_display(self):
        self.table.setRowHidden(4, False)

    def get_value(self, row):
        return float(self.table.item(row, 1).text())

    def get_operation(self):
        return self.combo['operations'].currentText()

    def get_display(self):
        return self.combo["display"].currentText()