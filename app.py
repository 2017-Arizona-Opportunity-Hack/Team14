from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form-selection.html')

@app.route('/transportation')
def transportation():
	return render_template('transportation-form.html')
  
@app.route('/medications')
def medications():
    return render_template('medications-form.html')

@app.route('/financial')
def financial():
	return render_template('financial-form.html')

if __name__ == '__main__':
	app.run()
