# 1: First Name
# 2: Middle Initial
# 3: Last Name
# 4: Date of Birth
# 5 Treatment Facility



class Parent:
    def __init__(self, fName, midInitial, lName, dob, treatFac):

        shared = {'First Name': fName, 'Middle Initial': midInitial, 'dob': dob, 'treatFac':treatFac}

class transportationForm(Parent):
    def __init__(self, transType, address, financialInformation, socialWorkerName,
                 socialWorkerSignature, financialNeedDescription, transportationProvider,
                 tripDate, tripCost, tripOrigin, tripDestination, travelDescription):

        shared = dict(Parent.shared)

        shared.append({'Transportation Type': transType, 'Address': address, 'Financial Information': financialInformation,
                       'Social Worker Name': socialWorkerName, 'Social Worker Signature': socialWorkerSignature,
                       'Financial Need Description': financialNeedDescription, 'Transportation Provider': transportationProvider,
                       'Trip Date': tripDate, 'Trip Cost': tripCost, 'Trip Origin': tripOrigin, 'Trip Destination': tripDestination,
                       'Travel Description': travelDescription})

        print (shared + "Transportation Type: " + transType + "\nAddress: " + address + "\nFinancial Information: " + financialInformation +
               "\nSocial Worker Signature: " + socialWorkerSignature + "\nFinancial Need Description: " + financialNeedDescription +
               "\nTransportation Provider: " + transportationProvider + "\nTrip Date: " + tripDate + "\nTrip Cost: " + tripCost +
               "\nTrip Origin: " + tripOrigin + "\nTrip Destination" + tripDestination + "\nTravel Description: " + travelDescription)

class medForm(Parent):
    def __init__(self, address, financialInformation, socialWorkerName,
                 medicationName, prescribingPhysician, dosage, dateApplied, quantities, refills, accepted):

        shared = dict(Parent.shared)

        shared.append(
            {'Address': address, 'Financial Information': financialInformation, 'Social Worker Name': socialWorkerName, 'Medication Name':
             medicationName, 'Prescribing Physician': prescribingPhysician, 'Dosage': dosage, 'Date Applied': dateApplied, 'Quantities': quantities,
             'Refills': refills, 'Accepted': accepted})

        print ("Address: " + address + "\nFinancial Information: " + financialInformation + "\nSocial Worker Name: " + socialWorkerName + "\nMedication Name: "
             + medicationName + "\nPrescribing Physician: " + prescribingPhysician + "\nDosage: " + dosage + "\nDate Applied: " + dateApplied +  "\nQuantities: " + quantities +
             "\nRefills: " + refills + "\nAccepted: " + accepted)
