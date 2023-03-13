from flask import Flask, render_template, request, redirect


class Jogo():
    def __init__(self, nome, categoria ,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('League of Legends','Moba','PC')
jogo2 = Jogo('Counter Strike: Global Offensive','Tiro','PC')
jogo3 = Jogo('Call os Duty','Tiro','PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)


@app.route('/criar', methods=['POST',])

def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    Jogo_new = Jogo(nome, categoria, console)
    lista.append(Jogo_new)
    return redirect('/')
    # return render_template('lista.html', titulo = 'Jogos', jogos=lista)


@app.route('/novo')

def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

app.run(debug=True)