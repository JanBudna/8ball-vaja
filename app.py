from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", spr = "Neki" )

@app.route("/eightball", methods = ["POST"])
def eightball():
    tmp = dict(request.form)
    vprašanje = tmp.get("vprašanje")

    if "ljubezen" in vprašanje:
        odg = "Kupi raje GPU."
    elif "vikend" in vprašanje:
        odg = "TikTok all day"
    elif "denar" in vprašanje:
        odg = "Burek only"
    elif "profesor" in vprašanje:
        odg = "F speedrun"
    elif "!" in vprašanje:
        odg = "Ne kriči"
    else:
        odgovori = ["Da", "Ne", "Mogoče", "Vprašaj kasneje"]
        odg = random.choice(odgovori)
    
    return render_template("index.html", rezultat = odg)

app.run(debug=True)