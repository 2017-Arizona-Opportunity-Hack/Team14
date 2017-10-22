# 1: First Name
# 2: Middle Initial
# 3: Last Name
# 4: Date of Birth
# 5 Treatment Facility

import csv

class transportationForm:
    def __init__(self, fName, midInitial, dob, treatFac, transType, address, financialInformation, socialWorkerName,
                 socialWorkerSignature, financialNeedDescription, transportationProvider,
                 tripDate, tripCost, tripOrigin, tripDestination, travelDescription):
        

        individual = {'First Name': fName, 'Middle Initial': midInitial, 'dob': dob, 'treatFac':treatFac, 'Transportation Type': transType, 'Address': address,         'Financial Information': financialInformation,
                       'Social Worker Name': socialWorkerName, 'Social Worker Signature': socialWorkerSignature,
                       'Financial Need Description': financialNeedDescription, 'Transportation Provider': transportationProvider,
                       'Trip Date': tripDate, 'Trip Cost': tripCost, 'Trip Origin': tripOrigin, 'Trip Destination': tripDestination,
                       'Travel Description': travelDescription}

        columnTitleRow = "First Name, Middle Initial, Date of Birth, Treatment Facility, Transportation Type, Address, Financial Information, Social Worker Name, Social Worker Signature, Financial Need Description, Transportation Provider, Trip Date, Trip Cost, Trip Origin, Trip Destination, Travel Description\n"

        with open('mycsvfile.csv', 'wb') as f:
            f.write(columnTitleRow)
            w = csv.writer(f)
            w.writerow(individual.values())

class medForm():
    def __init__(self, fName, midInitial, dob, treatFac, address, financialInformation, socialWorkerName,
                 medicationName, prescribingPhysician, dosage, dateApplied, quantities, refills, accepted):
        
        individual = {'First Name': fName, 'Middle Initial': midInitial, 'dob': dob, 'treatFac':treatFac,'Address': address, 'Financial Information': financialInformation, 'Social Worker Name': socialWorkerName, 'Medication Name':
             medicationName, 'Prescribing Physician': prescribingPhysician, 'Dosage': dosage, 'Date Applied': dateApplied, 'Quantities': quantities,
             'Refills': refills, 'Accepted': accepted}

        columnTitleRow = "First Name, Middle Initial, Date of Birth, Treatment Facility, Address, Financial Information, Social Worker Name, Medication Name, Prescribing Physician, Dosage," \
                         "Date Applied, Quantities, Refills, Accepted"
        csv.write(columnTitleRow)

        with open('mycsvfile.csv', 'wb') as f:
            f = csv.writer(f)
            w.writerow(individual.values())

foo = transportationForm("bailey","bailey","bailey","bailey","bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey", "bailey")
