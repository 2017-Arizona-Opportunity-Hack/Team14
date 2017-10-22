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

#************Add New Form Info here****************

#name of form should replace all instances of myForm in this block
#route here has to be the value of the of the dropdown in the form-selection.html for this form

#@app.route('/myForm')
#def myForm():
#    	return render_template('myForm.html')
		
#route here has to be the URL in the action on submit in the form's html

#@app.route('/myFormSubmit', methods=['POST'])
#def myFormSubmit():
#    kidneyData.start(json.dumps(request.form), 4) #this number is passed in and links up with the python script that is run to display the correct form type in the email.
#   return render_template('response.html')

#************End of Add New Form******************

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

@app.route('/returnHome', methods=['POST'])
def returnHome():
    return render_template('form-selection.html')

if __name__ == '__main__':
	app.run()
