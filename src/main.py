import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    message=os.getenv('MYAPP_MESSAGE', "Hello from MyAPP v2.0!")
    return message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('MYAPP_PORT', '8081'))
