from flask import Flask,render_template,request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/chatbot" ,methods =["POST"])
def chatbot():
    dataComing = request.form["data"]
    
    return dataComing

if __name__ == '__main__':
    app.run(debug=True)