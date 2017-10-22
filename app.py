from flask import Flask, render_template, jsonify

app = Flask(__name__)
  
@app.route("/medication-application")
def signUp():
    return render_template('medications-application-form.html')

@app.route("/medication-application", methods=['POST'])
def find():
    print(cool);

if __name__ == '__main__':
    app.run()
