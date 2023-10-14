from flask import Flask, render_template
import requests
import pandas as pd



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def api(word):
    """ Solution using dictionary api:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    """
    # Solution using dictionary.cvs
    df = pd.read_csv("dictionary.csv")

    definition = df.loc[df['word'] == word]['definition'].squeeze()
    print(definition)

    return {"word": word,
            "definition": definition}

app.run(debug=True, port=5001)