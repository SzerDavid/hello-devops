from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Hello! Az app fut a 8080 Porton."

'''
Mert magyarul szép az üzenet!
'''

'''
Bemutató!
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
