class ModelCalculator:
    def __init__(self):
        self.result = 0

    def calc(self, val1, operation, val2):
        if operation == '+':
            self.result = val1 + val2
        elif operation == '-':
            self.result = val1 - val2
        elif operation == '*':
            self.result = val1 * val2
        elif operation == '/':
            self.result = val1 / val2
        return self.result