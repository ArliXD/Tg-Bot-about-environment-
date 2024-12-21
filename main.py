from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello User</h1><a href="/random_fact">Привет, нажми сюда              </a><a href = "/random_coin">Нажми сюда,если хочешь поиграть в "Орел или Решка"</a> '


@app.route("/random_fact")
def random_fact():
    facts_list = ["У кошек не 9 жизней","Меня зовут не Алекс","Вода вскипает при 100 градусах"]
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/random_coin")
def random_coin():
    facts_list = ["Орел","Решка"]
    return f'<p>{random.choice(facts_list)}</p>'

app.run()
