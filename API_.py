from Scrapy_ import returnApi
import json
from flask import Flask,render_template

app = Flask(__name__)
datas = json.loads(returnApi())
@app.route("/")
def index():
    return render_template('index2.html',datas=datas)

if __name__ == '__main__':
    app.run(debug="True",host="127.0.0.1",port='5001')