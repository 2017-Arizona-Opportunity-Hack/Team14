# 1: First Name
# 2: Middle Initial
# 3: Last Name
# 4: Date of Birth
# 5 Treatment Facility

import csv

class Parent:
    def __init__(self, fName, midInitial, lName, dob, treatFac):

        shared = {'First Name': fName, 'Middle Initial': midInitial, 'dob': dob, 'treatFac':treatFac}

class transportationForm(Parent):
    def __init__(self, transType, address, financialInformation, socialWorkerName,
                 socialWorkerSignature, financialNeedDescription, transportationProvider,
                 tripDate, tripCost, tripOrigin, tripDestination, travelDescription):

        shared = dict(Parent.shared)

        individual = shared.append({'Transportation Type': transType, 'Address': address, 'Financial Information': financialInformation,
                       'Social Worker Name': socialWorkerName, 'Social Worker Signature': socialWorkerSignature,
                       'Financial Need Description': financialNeedDescription, 'Transportation Provider': transportationProvider,
                       'Trip Date': tripDate, 'Trip Cost': tripCost, 'Trip Origin': tripOrigin, 'Trip Destination': tripDestination,
                       'Travel Description': travelDescription})

        columnTitleRow = "Transportation Type, Address, Financial Information, Social Worker Name, Social Worker Signature, Financial Need Description" \
                         "Transportation Provider, Trip Date, Trip Cost, Trip Origin, Trip Destination, Travel Description\n"
        csv.write(columnTitleRow)

        with open('mycsvfile.csv', 'wb') as f:
            w = csv.writer(f)
            w.writerow(individual.values())
class medForm(Parent):
    def __init__(self, address, financialInformation, socialWorkerName,
                 medicationName, prescribingPhysician, dosage, dateApplied, quantities, refills, accepted):

        shared = dict(Parent.shared)

        individual = shared.append(
            {'Address': address, 'Financial Information': financialInformation, 'Social Worker Name': socialWorkerName, 'Medication Name':
             medicationName, 'Prescribing Physician': prescribingPhysician, 'Dosage': dosage, 'Date Applied': dateApplied, 'Quantities': quantities,
             'Refills': refills, 'Accepted': accepted})

        columnTitleRow = "Address, Financial Information, Social Worker Name, Medication Name, Prescribing Physician, Dosage," \
                         "Date Applied, Quantities, Refills, Accepted"
        csv.write(columnTitleRow)

        with open('mycsvfile.csv', 'wb') as f:
            w = csv.writer(f)
            w.writerow(individual.values())