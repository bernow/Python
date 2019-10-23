from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello World"

@app.route("/html")
def html():
    return "<h1> This is HTML h1 tag! </h1>"

@app.route("/d_day")
def d_day():
    today = datetime.now()
    finish = datetime(2019,11,27)
    remain = finish - today
    return f'우리가 같이 있을 수 있는 시간이 이제 {remain}일 밖에 안남았어...ㅠㅠ'

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route('/myday')
def myday():
    today = datetime.now()
    return render_template('myday.html', today=today)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('pong.html', name=name, age=age)

@app.route('/god')
def a():
    return render_template('god.html')

@app.route('/godAnswer')
def b():
    name = request.args.get('name')
    stats = ['천재', '악당', '쭈구리', '배고픔', '고운', '도련님']
    stats2 = random.sample(stats,3)
    return render_template('godAnswer.html',name=name, stats=stats2)