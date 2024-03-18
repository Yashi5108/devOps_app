from flask import Flask

app  = Flask(__name__)

@app.route('/',methods=["POST", "GET"])
def testing():
    a = "Hello Wolrd!.."
    return {"status":a}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)