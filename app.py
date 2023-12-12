from flask import Flask,render_template

app = Flask(__name__, static_folder='./templates/image')



app = Flask(__name__)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

#「/templates」へアクセスがあった場合に、index.htmlを返す
#@app.route("/index")
#def index():
#    return render_template("index.html")

#「/templates」へアクセスがあった場合に、index.htmlを返す
@app.route("/index.html", methods=["GET"])
def index():
    return render_template("index.html")

#「/nextpage」へアクセスがあった場合に、next_index.htmlを返す
@app.route("/menu.html", methods=["GET"])
def nextpage():
    return render_template("menu.html")








#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)



