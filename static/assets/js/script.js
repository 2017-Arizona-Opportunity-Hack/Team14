var index = 0;

function addMedication() {
    
    var medication = {
        name: document.getElementById("medication-name").value,
        dosage: document.getElementById("medication-dosage").value,
        quantity: document.getElementById("medication-quantity").value,
        physician: document.getElementById("medication-physician").value,
        month: document.getElementById("medication-dateapplied-month").value,
        day: document.getElementById("medication-dateapplied-day").value,
        year: document.getElementById("medication-dateapplied-year").value,
        refills: "",
        status: "",
        covered: ""
    }
    
    if (document.getElementById("medication-refills-yes").checked == true) {
        medication.refills = "yes";
    } else if (document.getElementById("medication-refills-no").checked == true) {
        medication.refills = "no";
    }
    
    if (document.getElementById("medication-status-pending").checked == true) {
        medication.status = "pending";
    } else if (document.getElementById("medication-status-accepted").checked == true) {
        medication.status = "accepted";
    } else if (document.getElementById("medication-status-denied").checked == true) {
        medication.status = "denied";
    }
    
    if (document.getElementById("medication-covered-yes").checked == true) {
        medication.covered = "yes";
    } else if (document.getElementById("medication-covered-no").checked == true) {
        medication.covered = "no";
    }
    
    index++;
    
    var output = document.getElementById("medication-entry").innerHTML.toString();
    var replace = "medication" + index + "\-";
    output = output.replace(/medication\-/g , replace);
    
    document.getElementById(("medication" + index)).innerHTML = output;
    
    // Refill input
    document.getElementById(replace + "name").value = medication.name;
    document.getElementById(replace + "dosage").value = medication.dosage;
    document.getElementById(replace + "quantity").value = medication.quantity;
    document.getElementById(replace + "physician").value = medication.physician;
    document.getElementById(replace + "dateapplied-month").value = medication.month;
    document.getElementById(replace + "dateapplied-day").value = medication.day;
    document.getElementById(replace + "dateapplied-year").value = medication.year;
    if (medication.refills == "yes") {
        document.getElementById(replace + "refills-yes").checked = true;
    } else if (medication.refills == "no"){
        document.getElementById(replace + "refills-no").checked = true;
    }
    if (medication.status == "pending") {
        document.getElementById(replace + "status-pending").checked = true;
    } else if (medication.status == "accepted") {
        document.getElementById(replace + "status-accepted").checked = true;
    } else if (medication.status == "denied") {
        document.getElementById(replace + "status-denied").checked = true;
    }
    if (medication.covered == "yes") {
        document.getElementById(replace + "covered-yes").checked = true;
    } else if (medication.covered == "no") {
        document.getElementById(replace + "covered-no").checked = true;
    }
    
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