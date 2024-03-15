// Sticky navbar
// Declare variables
let navbar = document.getElementById("navbar");
let navOffset = navbar.offsetTop;

function navBarStick() {
    // Check if navbar is at or past top of screen, if so, stick
    if (window.pageYOffset >= navOffset) {
        navbar.classList.add("stickToTop")
    }
    else {
        navbar.classList.remove("stickToTop")
    }
}
// Check if navbar should stick on scroll
window.onscroll = function() {navBarStick()};

// Slick carrosel
$('.slider').slick({
    accessibility: true,
    autoplay: true,
    prevArrow:"<img class='carrosel-left carrosel-arrow' src='resources/left.svg'>",
    nextArrow:"<img class='carrosel-right carrosel-arrow' src='resources/right.svg'>"
});


// Date input check
// Get current day information
let today = new Date();
// Get day, month and year
let day = today.getDate();
let month = today.getMonth() + 1;
let year = today.getFullYear();


// Make sure month and day are in correct format
if (month < 10) {
    month = 0 + String(month)
}
if (day < 10) {
    day = 0 + String(month)
}
// Concatenate dates into correct format
let minDate = String(year)+"-"+String(month)+"-"+String(day)
// Apply minimum date
let dateInput = document.getElementById("dateInput");
dateInput.setAttribute("min",minDate)


// Dropdown selection
function dropdownChange() {
    let dropdown = document.getElementById('dropdown');
    let value = dropdown.value;

    switch(value) {
        case '1':
            document.getElementById("advice").innerHTML="Childhood vaccines: A disclaimer that multiple vaccines are normally administered in combination and may cause the child to be sluggish or feverous for 24 – 48 hours afterwards.";
            break;
        case '2':
            document.getElementById("advice").innerHTML="Influenza: The best time to get vaccinated is in April and May each year for optimal protection over the winter months.";
            break;
        case '3':
            document.getElementById("advice").innerHTML="Covid Booster Shot: Advice that everyone should arrange to have their third shot as soon as possible and adults over the age of should have their fourth shot to protect against new variant strains.";
            break;
        case '4':
            document.getElementById("advice").innerHTML="Blood test: That some tests require some fasting ahead of time and that a staff member will advise them on this prior to the appointment.";
            break;
    }
}


// Form validation
function formValidate() {
    // Check if js form validation is disabled
    if (!$('#jsformnovalidate').is(":checked")) {

        // Check at least a checkbox was selected
        let validCheckboxes = false
        let checkboxes = document.querySelectorAll('input[type="checkbox"]');
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                validCheckboxes = true;
                break;
            }
        }

        // Define dropdown and patient id variables
        let patientId = document.getElementById('patientId').value;
        let upperPatientId = patientId.toUpperCase();
        let dropdown = document.getElementById('dropdown');
        let value = dropdown.value;
        
        // Check if form is valid
        if (!upperPatientId.match(/[A-Z]{2}[0-9]+[A-Z]{1}/)) {
            document.getElementById("errorText").innerHTML="Your patientId is incorrect";
            return false;
        }
        else if (validCheckboxes == false) {
            document.getElementById("errorText").innerHTML="You need to select a time";
            return false;
        }
        else if (value == '0') {
            document.getElementById("errorText").innerHTML="You need to select an appointment reason";
            return false;
        }
        else
            return true;
    }
}