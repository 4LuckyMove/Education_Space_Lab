class PresenterCalculator:
    def __init__(self, demo_view, demo_model):
        self.model = demo_model
        self.view = demo_view

        self.view.set_options('operations', ['+', '-', '*', '/'])
        self.view.set_options('display', ['Вывод в консоль', 'Обновить результат', 'Вывести и обновить'])
        self.printToScreen = True
        self.view.hide_display()

        self.view.btnSignal.connect(self.handle_button)
        self.view.displaySignal.connect(self.display_update)

    def display_update(self):
        display = self.view.get_display()
        if display == 'Обновить результат':
            self.printToScreen = False
            self.view.show_display()
        elif display == 'Вывод в консоль':
            self.printToScreen = True
            self.view.show_display()
        else:
            self.printToScreen = True
            self.view.show_display()

    def handle_button(self):
        val1 = self.view.get_value(0)
        operation = self.view.get_operation()
        val2 = self.view.get_value(2)
        result = self.model.calc(val1, operation, val2)

        if self.printToScreen:
            print(result)
        self.view.setResult(result)