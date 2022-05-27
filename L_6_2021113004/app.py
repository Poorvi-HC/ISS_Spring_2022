from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/calc/sum', methods = ['POST','GET'])
def sum():
    if request.method == 'POST':
        n1 = request.form['no1']
        n2 = request.form['no2']
        try:
            result = int(n1) + int(n2)
            return str(result)
        except:
            return 'invalid syntax'

    return render_template('sum.html')

@app.route('/')
def ret():
    return "Hello"

@app.route('/calc/multiply', methods = ['POST','GET'])
def multiply():
    if request.method == 'POST':
        n1 = request.form['no1']
        n2 = request.form['no2']
        try:
            result = int(n1) * int(n2)
            return str(result)
        except:
            return 'invalid syntax'

    return render_template('prod.html')

if __name__ == '__main__':
    app.run(debug=True)