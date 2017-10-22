var medications = [];

function addMedication() {
    
    var medication = {
        name: document.getElementById("medication-name"),
        dosage: document.getElementById("medication-dosage"),
        quantity: document.getElementById("medication-quantity"),
        physician: document.getElementById("medication-physician"),
        month: document.getElementById("medication-dateapplied-month"),
        day: document.getElementById("medication-dateapplied-day"),
        year: document.getElementById("medication-dateapplied-year"),
        refills: document.getElementById("medication-refills"),
        status: document.getElementById("medication-status"),
        covered: document.getElementById("medication-covered")
    }
    
    medications.push(medication);
    
    output = "<h4 style=\"text-align: center\">";
    
    if (medications.length == 1) {
        output += "1 Medication Added!</h4>";
    } else {
        output += medications.length + " Medications Added!</h4>";
    }
    
    document.getElementById("medications").innerHTML = output;
    
    // Reset Input
    document.getElementById("medication-name").value = "";
    document.getElementById("medication-dosage").value = "";
    document.getElementById("medication-quantity").value = "";
    document.getElementById("medication-physician").value = "";
    document.getElementById("medication-dateapplied-month").value = "00";
    document.getElementById("medication-dateapplied-day").value = "00";
    document.getElementById("medication-dateapplied-year").value = "";
    document.getElementById("medication-refills-yes").checked = false;
    document.getElementById("medication-refills-no").checked = false;
    document.getElementById("medication-status-pending").checked = false;
    document.getElementById("medication-status-accepted").checked = false;
    document.getElementById("medication-status-denied").checked = false;
    document.getElementById("medication-covered-yes").checked = false;
    document.getElementById("medication-covered-no").checked = false;
}