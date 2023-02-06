from flask import Flask, render_template
app = Flask(__name__)

import datetime
adesso = int(datetime.datetime.now().time().hour)
if adesso >=0:
    buon="buongiorno"
elif adesso>=12:
     buon="buon pranzo"
elif adesso>=16:
     buon="buon pomeriggio"
elif adesso>=19:
     buon="buona cena"
elif adesso>=22:
     buon="buona notte"


@app.route('/')
@app.route('/en')
def hello_world():
  return render_template("indexcss.html", Titolo='Welcome', Testo='Hello, world!',immagine='static/images/download.png')


@app.route('/it')
def ciao_mondo():
  return render_template("indexcss.html", Titolo='Benvenuti', Testo=buon,immagine='static/images/download.png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)