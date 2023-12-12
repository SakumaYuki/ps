from flask import Flask,render_template

app = Flask(__name__, static_folder='./templates/image')

app = Flask(__name__)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

#「/templates」へアクセスがあった場合に、index.htmlを返す
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/index/menu')
def menu_page():
  return render_template('menu.html')

@app.route("/index/fake-sns")
def another_page():
  return render_template('fake-sns.html')








#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)



