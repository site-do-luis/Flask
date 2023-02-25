from flask import Flask, render_template


class Jogo():
    def __init__(self, nome, categoria ,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')

def ola():
    titulo = 'Jogos'
    jogo1 = Jogo('League of Legends','Moba','PC')
    jogo2 = Jogo('Counter Strike: Global Offensive','Tiro','PC')
    jogo3 = Jogo('Call os Duty','Tiro','PS2')
    jogo4 = Jogo('Need for Speed','Corrida','PS2')
    lista = [jogo1, jogo2, jogo3, jogo4]
    return render_template('lista.html', titulo = titulo, jogos=lista)


@app.route('/novo')

def novo():
    titulo = 'Novo Jogo'
    return render_template('novo.html', titulo = titulo)

app.run(debug=True)