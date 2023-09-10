from flask import Flask

#"this function imports Flask to my code"
app = Flask(__name__)

#this functions directs the program where to get some templets 

@app.route("/")
def HBNB():
    return "<p>HELLO HBNB!</p>"

app.url_map.strict_slashes=False

@app.route("/hbnb")
def HBNB_1():
    return "<p> HBNB </p>"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)