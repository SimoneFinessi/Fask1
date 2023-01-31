from flask import Flask
app = Flask(__name__)
print("ciao ")
@app.route('/', methods=['GET'])
def hello_world():
    x=1
    return(str(x+1)+"<br>"+'<h1>ciao, mondo!</h1>')

@app.route('/en', methods=['GET'])
def inglese():
    return("hello word")
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)