from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dictionary.html")

@app.route("/api/v1/<word>")
def api(word):
    definition = "The word´s definition"
    return (definition)

app.run(debug=True)