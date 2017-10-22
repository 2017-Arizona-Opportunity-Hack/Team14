from flask import Flask, render_template

app = Flask(__name__)
  
@app.route("/")
def signUp():
    return render_template('medications-applicationform.html')

app.run()
