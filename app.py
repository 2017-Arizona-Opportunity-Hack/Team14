from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('form-selection.html')

@app.route("/transportation")
def transportation():
    alert("I AM IN FLASH")
    return render_template('transportation-form.html');
  
@app.route('/medication-application')
def signUp():
<<<<<<< HEAD
    return render_template('medications-application-form.html')

@app.route('/medication-application-analysis', methods = ['POST'])
def cool():
    return render_template('FormSelection.html');
=======
	return render_template('medications-form.html')
>>>>>>> a4fd2f592453dfb350972eb03c8a4b7dae9847a1

@app.route("/english-financial")
def financial():
    return render_template('financial-form.html');

if __name__ == '__main__':
    app.run()