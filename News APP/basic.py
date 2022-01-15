from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/')
def index():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=46caf2e6f66e428c95e3fbe4ecf91475"
    r=requests.get(url).json()

    cases ={
        'articles' : r['articles']
    }
    

    return render_template("index.html",case=cases)


if __name__=='__main__':
    app.run(debug=True)
