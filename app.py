import os
import pymysql

from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


def conectar_banco():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def home():
    return render_template('index.html', active='home')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', active='sobre')


@app.route('/contato', methods=['GET', 'POST'])
def contato():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        conexao = conectar_banco()

        try:
            with conexao.cursor() as cursor:
                sql = """
                    INSERT INTO contatos (nome, email, assunto, mensagem)
                    VALUES (%s, %s, %s, %s)
                """

                cursor.execute(sql, (nome, email, assunto, mensagem))

            conexao.commit()
            flash('Comentário enviado com sucesso!', 'success')

        except pymysql.MySQLError as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar contato: {erro}')
            flash('Não foi possível enviar seu comentário.', 'danger')

        finally:
            conexao.close()

        return redirect(url_for('contato'))

    return render_template('contato.html', active='contato')


@app.route('/listar')
def listar():

    conexao = conectar_banco()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('SELECT * FROM contatos ORDER BY id DESC')
            contatos = cursor.fetchall()

    finally:
        conexao.close()

    return render_template('listar.html', contatos=contatos, active='listar')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)