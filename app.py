from flask import Flask,render_template

app = Flask(__name__)
app = Flask(__name__, static_folder='/template/image') 
app = Flask(__name__, static_folder='./template/image')

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

@app.route("/fake-sns.html", methods=["GET"])
def fakesns_page():
    return render_template("fake-sns.html")

@app.route("/fake-mail.html", methods=["GET"])
def fakemail_page():
    return render_template("fake-mail.html")

@app.route("/new_account.html", methods=["GET"])
def newaccount_page():
    return render_template("new_account.html")

@app.route("/product_d.html", methods=["GET"])
def productd_page():
    return render_template("product_d.html")

@app.route("/eventlist.html", methods=["GET"])
def eventlist_page():
    return render_template("eventlist.html")

@app.route("/eventdetail.html", methods=["GET"])
def eventdetail_page():
    return render_template("eventdetail.html")




#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)



