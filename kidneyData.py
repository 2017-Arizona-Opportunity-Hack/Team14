import csv
import json


class form():

        def __init__(self, dictionary, formNum):

            str = ''

            if formNum == 1:
                str = 'medicalform.csv'
            elif formNum == 2:
                str = 'transportationform.csv'
            elif formNum == 3:
                str = 'financialform.csv'
            else:
                str = 'form.csv'

            filename = dictionary['lastname'] + dictionary['firstname'] + str

            with open(filename, 'w') as f:
                w = csv.writer(f)
                w.writerow(dictionary.keys())
                w.writerow(dictionary.values())
            f.close()


def start(jsonString, formNum):
    python_object = json.loads(jsonString)
    foo = form(python_object, formNum)

