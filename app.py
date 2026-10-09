from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', active='home')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', active='sobre')


@app.route('/contato')
def contato():
    return render_template('contato.html', active='contato')


if __name__ == '__main__':
    # host='0.0.0.0' permite acessar pelo IP público da EC2
    app.run(debug=False, host='0.0.0.0', port=5000)
