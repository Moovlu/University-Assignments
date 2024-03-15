<?php
    $pageName = 'Booking';
    require_once("tools.php");
    require_once("segments/head.php");
?>
            <nav>
                <div id="navbar">
                    <a href="index.php">Back</a>
                </div>
            </nav>
        </div>

        <main>
            <form method="post" name="bookingForm" onsubmit="return formValidate()">
                <div class="formContainer">
                    <p class="gridItem">Patient Id</p>
                    <input name="pid" value="<?php echo isset($_POST['pid']) ? $_POST['pid'] : '' ?>" type="text" required class="gridItem" id="patientId">
                    <p class="gridItem">Date</p>
                    <input name="date" value="<?php echo isset($_POST['date']) ? $_POST['date'] : '' ?>" type="date" required class="gridItem" id="dateInput">
                    <p class="gridItem">Time</p>
                    <div>
                        <label class="checklistItem">
                            <input name="time1" type="checkbox" class="gridItem">
                            <span class="checklistLabel leftPill">9am - 12pm</span>
                        </label><label class="checklistItem">
                            <input name="time2" type="checkbox" class="gridItem">
                            <span class="checklistLabel">12pm - 3pm</span>
                        </label><label class="checklistItem">
                            <input name="time3" type="checkbox" class="gridItem">
                            <span class="checklistLabel rightPill">3pm - 6pm</span>
                        </label>
                    </div>
                    <p class="gridItem">Appointment Reason</p>
                    <select name="reason" class="gridItem" id="dropdown" onchange="dropdownChange()">
                        <option value="0" selected disabled hidden>Please select a value</option>
                        <option value="1">Childhood Vaccination Shots</option>
                        <option value="2">Influenza Shot</option>
                        <option value="3">Covid Booster Shot</option>
                        <option value="4">Blood Test</option>
                    </select>
                    <p class="gridItem">Advice</p>
                    <p class="gridItem center" id="advice">None Selected</p>
                    <p class='griditem'>Submit without Javascript validation</p>
                    <input type='checkbox' id='jsformnovalidate'>
                </div>
                <input name="submitBooking" type="submit" class="gridItem" value="Regular submit">
                <input name="submitBooking" type="submit" formnovalidate="formnovalidate" value="Submit without HTML validation">
            </form>
            <?php echo $outputMessage; ?>
            <p id="errorText"></p>
        </main>

<?php require_once("segments/footer.php"); ?>