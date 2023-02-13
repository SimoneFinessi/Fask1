from flask import Flask#libreria che permette di ostare siti web
app = Flask(__name__)

print("ciao ")
@app.route('/', methods=['GET'])
def hello_world():
    x=1
    return(str(x+1)+"<br>"+'<h1 style="color:#ff0000">scrivi it o en dopo lo /</h1>')

@app.route('/en', methods=['GET'])
def inglese():
    return("hello word!")

@app.route('/it', methods=['GET'])
def ita():
    return("ciao mondo!")
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)