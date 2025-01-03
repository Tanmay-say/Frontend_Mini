from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")  # Remove the stray 'main'

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/index2.html")
def index2():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Only one call to app.run is needed
