from flask import Flask,render_template

app = Flask(__name__)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

#「/templates」へアクセスがあった場合に、index.htmlを返す
@app.route("/templates")
def index():
    return render_template("index.html")

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)



