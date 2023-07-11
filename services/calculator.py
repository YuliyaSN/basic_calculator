class CalculatorService:
    def generate_equality(self, sequence):
        return ''.join(sequence)

    def calculate(self, sequence):
        equality = self.generate_equality(sequence)
        return eval(equality)
