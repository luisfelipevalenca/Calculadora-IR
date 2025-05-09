from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular():
    salario = request.form.get('salario')
    if salario:
        salario = float(salario.replace(',', '.'))
        if salario <= 2428.80:
            aliquota = 0
        elif salario <= 2826.65:
            aliquota = 7.5
        elif salario <= 3751.05:
            aliquota = 15.0
        elif salario <= 4664.68:
            aliquota = 22.5
        else:
            aliquota = 27.5
        desconto = round(salario * (aliquota / 100), 2)
        liquido = round(salario - desconto, 2)
        return render_template('index.html', salario=salario, aliquota=aliquota, desconto=desconto, liquido=liquido)
    return render_template('index.html', salario=None)

if __name__ == '__main__':
    app.run(debug=True)
