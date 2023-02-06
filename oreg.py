from flask import Flask, render_template
app = Flask(__name__)

import datetime
adesso = int(datetime.datetime.now().time().hour)
if adesso >=0:
    buon="buongiorno"
    immag="static/images/buongiorno.jpg"
if adesso>=12:
     buon="buon pranzo"
     immag="static/images/pranzo.jpg"
if adesso>=16:
     buon="buon pomeriggio"
     immag="static/images/pomeriggio.jpg"
if adesso>=19:
     buon="buona cena"
     immag="static/images/cena.jpg"
if adesso>=22:
     buon="buona notte"
     immag="static/images/sera.jpg"


@app.route('/')
@app.route('/en')
def hello_world():
  return render_template("indexcss.html", Titolo='Welcome', Testo=buon,immagine=immag)


@app.route('/it')
def ciao_mondo():
  return render_template("indexcss.html", Titolo='Benvenuti', Testo=buon,immagine=immag)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)