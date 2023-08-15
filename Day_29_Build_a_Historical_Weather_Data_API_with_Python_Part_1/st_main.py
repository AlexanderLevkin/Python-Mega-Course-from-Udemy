from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home1():
    return render_template("home1.html")


@app.route("/api/v1/<your_word>")
def about(your_word: str):
    definition = your_word.upper()
    return {
        "your_word": your_word,
        "definition": definition
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
