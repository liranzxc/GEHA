from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

def GetResultFromExcel(user_id,keywords):
    file = 'data.xlsx'
    pd.set_option('display.max_colwidth', -1) # display enitre coloums
    # Load spreadsheet
    xl = pd.ExcelFile(file)
    # Print the sheet names
    df1 = xl.parse('גיליון1')
    return df1[df1["Patient"] == user_id][keywords].to_string()



def ResponseBot(dataComing):
    # get keywords

    medicalKeyWords = ["med","MED","תרופות"]
    keywords = []
    print(dataComing)
    if any(keyword in dataComing for keyword in medicalKeyWords ):
        keywords.append("Med")
    

    ## finish keywords

    return GetResultFromExcel(user_id=3320,keywords=keywords) 

@app.route("/")
def login():
    return render_template("index.html",token="BASDSADADSADADAAD")


@app.route("/chatbot" ,methods =["POST"])
def chatbot():
    dataComing = request.form["data"]
    
    return ResponseBot(dataComing)


@app.route("/test",methods=["POST"])
def test():
    print(request.form["name"])

    return "Good job"

if __name__ == "__main__":
    app.run(debug=True)



