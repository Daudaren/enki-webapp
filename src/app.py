from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generic.html')
def generic():
    return render_template('generic.html')


@app.route('/elements.html')
def elements():
    return render_template('elements.html')

@app.route('/employees.html')
def employees():
    return render_template('employees.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
