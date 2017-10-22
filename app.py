from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('FormSelection.html')

@app.route("/transportation")
def transportation():
    return render_template('transportation-form.html')
  
@app.route("/medication-application")
def signUp():
    return render_template('medications-application-form.html')

<<<<<<< HEAD
@app.route("/medication-application", methods=['POST'])
def find():
    print(cool);
=======
@app.route("/english-financial")
def financial():
    return render_template('financial-form.html');

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)
>>>>>>> f12f712960e592dcad52ccad05588dd2c5a0b868

if __name__ == '__main__':
    app.run()
