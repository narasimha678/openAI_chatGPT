Python Flask API

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        result = int(value1) + int(value2)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()

HTML Page

<html>
    <head>
        <title>Add two values</title>
    </head>
    <body>
        <h1>Add two values</h1>
        <form action="/result" method="POST">
            Value 1: <input type="text" name="value1"><br>
            Value 2: <input type="text" name="value2"><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>

Result HTML Page

<html>
    <head>
        <title>Result</title>
    </head>
    <body>
        <h1>Result</h1>
        <p>The result is {{ result }}</p>
    </body>
</html>