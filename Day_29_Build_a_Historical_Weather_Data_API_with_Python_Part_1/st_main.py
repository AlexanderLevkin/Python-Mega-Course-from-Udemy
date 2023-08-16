from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

df = pd.read_csv('../Day_29_Build_a_Historical_Weather_Data_API_with_Python_Part_1/dictionary.csv')
print(df['word'])



@app.route("/")
def home1():
    return render_template("home1.html")


@app.route("/api/v1/<your_word>")
def about(your_word: str):
    definition = df.loc[df['word'] == your_word]['definition'].squeeze()
    return {
        "your_word": your_word,
        "definition": definition
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
