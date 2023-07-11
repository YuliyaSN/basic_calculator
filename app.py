from flask import Flask, jsonify, render_template, request

from services.calculator import CalculatorService

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calculator.html')


@app.route('/calculate', methods=["POST"])
def calculate():
    content = request.json
    number_1 = content.get('number_1')
    number_2 = content.get('number_2')
    operator = content.get('operator')

    sequence = [number_1, operator, number_2]
    service = CalculatorService()
    result = service.calculate(sequence)

    return jsonify({'result': result})


if '__main__' == __name__:
    app.run()
