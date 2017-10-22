from flask import Flask, render_template, jsonify, request
import csv, kidneyData, json

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

@app.route('/medicationsFormSubmit', methods=['POST'])
def medicationsFormSubmit():
    kidneyData.start(json.dumps(request.form), 1)
    return render_template('response.html')

@app.route('/transportationFormSubmit', methods=['POST'])
def transportationFormSubmit():
    kidneyData.start(json.dumps(request.form), 2)
    return render_template('response.html')

@app.route('/financialFormSubmit', methods=['POST'])
def financialFormSubmit():
    kidneyData.start(json.dumps(request.form), 3)
    return render_template('response.html')

@app.route('/thanksFormSubmit', methods=['POST'])
def thanksFormSubmit():
    return render_template('form-selection.html')

if __name__ == '__main__':
	app.run()
