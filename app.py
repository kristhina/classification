from flask import Flask, render_template, request, redirect
from classification_helper import df, bold_word, list_okna, list_klimatyzacja, list_kuchnia
import json

app = Flask(__name__)


@app.route('/<number>', methods=['GET', 'POST'])
def classifier(number):
    num = int(number)
    description = df['opis'][num]
    nt = bold_word(description, list_okna, "Blue")
    nt = bold_word(nt, list_klimatyzacja, "Red")
    nt = bold_word(nt, list_kuchnia, "Green")
    if request.method=="POST":
        okna = request.form.get("okna")
        klima = request.form.get("klima")
        kuchnia = request.form.get("kuchnia")
        my_json = {"description": description, "okna": okna, "klima": klima, "kuchnia": kuchnia}
        f = open("test.txt", "a")
        json.dump(my_json, f)
        f.close()
        new_url = "/{}".format(num+1)
        return redirect(new_url)
    return render_template("index.html", nt=nt, number=number)


app.run(debug=True)