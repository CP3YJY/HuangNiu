from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/index1')
def index1():  # put application's code here
    return render_template('index1.html')

@app.route('/wordCould')
def wordCould():  # put application's code here
    return render_template('wordCould.html')

@app.route('/wordCould1')
def wordCould1():  # put application's code here
    return render_template('wordCould1.html')

@app.route('/area')
def area():  # put application's code here
    return render_template('area.html')

@app.route('/area1')
def area1():  # put application's code here
    return render_template('area1.html')

@app.route('/list')
def list():  # put application's code here
    return render_template('list.html')

@app.route('/list1')
def list1():  # put application's code here
    return render_template('list1.html')

@app.route('/emo')
def emo():  # put application's code here
    return render_template('emo.html')

@app.route('/emo1')
def emo1():  # put application's code here
    return render_template('emo1.html')

@app.route('/xian')
def xian():  # put application's code here
    return render_template('xian.html')

@app.route('/xian1')
def xian1():  # put application's code here
    return render_template('xian1.html')

if __name__ == '__main__':
    app.run()
