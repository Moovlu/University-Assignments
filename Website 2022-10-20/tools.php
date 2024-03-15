<?php
    session_start();

    // Booking Page
    $outputMessage = "";
    if (isset($_POST["submitBooking"]))
    {
        // PatientID sanitisation
        $sanitisedPid = trim($_POST["pid"]);
        $sanitisedPid = htmlspecialchars($sanitisedPid);
        $sanitisedPid = strtoupper($sanitisedPid);

        // PatientID validation
        if (!preg_match("/[A-Z]{2}[0-9]+[A-Z]{1}/", $sanitisedPid)) {
            $outputMessage = "<p>PatientID is invalid</p>";
        // Date validation
        } elseif (strtotime($_POST["date"]) < strtotime('now')) {
            $outputMessage = "<p>Date is invalid</p>";
        // Check a time was selected
        } elseif (!(isset($_POST["time1"])||isset($_POST["time2"])||isset($_POST["time3"]))) {
            $outputMessage = "<p>Please pick a time</p>";
        // Check a reason was selected
        } elseif (empty($_POST["reason"])) {
            $outputMessage = "<p>Please pick a reason</p>";
        // Success!
        } else {
            // Write data to appointments.csv
            $outputMessage = "<p>Data successfully submitted! The office will be in touch soon.</p><a href='index.php'>Back</a>";
            switch ($_POST["reason"]) {
                case 1:
                    $reason = "Childhood Vaccination Shots";
                    break;
                case 2:
                    $reason = "Influenza Shot";
                    break;
                case 3:
                    $reason = "Covid Booster Shot";
                    break;
                case 4:
                    $reason = "Blood Test";
                    break;
            }
            $fp = fopen('appointments.txt', 'a');
            $writeOutput = array(
                $sanitisedPid,
                $_POST["date"],
                isset($_POST["time1"]),
                isset($_POST["time2"]),
                isset($_POST["time3"]),
                $reason,
                date("Y/m/d H:i:s")
            );

            fputcsv($fp, $writeOutput);
            fclose($fp);
        }
    }

    // Login Form
    $loginMessage = "";
    if (isset($_POST["submitLogin"])) {
        $loginMessage = "Login invalid, please try again";
        // Open users file and write into array
        $fp = fopen('users.txt', 'r');
        flock($fp, LOCK_SH);
        while (($data = fgetcsv($fp)) !== false) {
            $array[] = $data;
        }
        $foundLogin = false;
        // See if username input is valid, compare password if valid
        for ($i = 0; $i < count($array); $i++) {
            if ($_POST['usernameInput'] == $array[$i][0] && $_POST['passwordInput'] == $array[$i][1]) {
                $_SESSION['username'] = $array[$i][0];
                $foundLogin = true;
                break;
            }
        }
        fclose($fp);
        // Report failed login
        if (!$foundLogin) {
            $fp = fopen('accessattempts.txt', 'a');
                $failedLoginOutput = array(
                    $_POST["usernameInput"],
                    date('Y/m/d H:i:s')
                );
                fputcsv($fp, $failedLoginOutput);
                fclose($fp);
        }
    }
    
    // Logout functionality
    if (isset($_POST["logout"])) {
        session_destroy();
        header("Refresh:0");
    }

    // Create new User form
    $addLoginMessage = "";
    if (isset($_POST["submitNewUser"])) {
        // Check both inputs are filled
        $addLoginMessage = "One or more fields have been left blank!";
        if (!(empty($_POST["newUsernameInput"]) && empty($_POST["newPasswordInput"]))) {
            // Open users file and write into array
            $fp = fopen('users.txt', 'r');
            flock($fp, LOCK_SH);
            while (($data = fgetcsv($fp)) !== false) {
                $array[] = $data;
            }
            // See if username input is duplicate
            $foundUsername = false;
            for ($i = 0; $i < count($array); $i++) {
                if ($_POST['newUsernameInput'] == $array[$i][0]) {
                    $addLoginMessage = "User already exists!";
                    $foundUsername = true;
                    break;
                }
            }
            // Write to users if input is unique
            fclose($fp);
            if (!$foundUsername) {
                $fp = fopen('users.txt', 'a');
                $writeUsersOutput = array(
                    $_POST["newUsernameInput"],
                    $_POST["newPasswordInput"]
                );
                fputcsv($fp, $writeUsersOutput);
                fclose($fp);
                $addLoginMessage = "Successfully made new user";
            }
        }
    }
?>