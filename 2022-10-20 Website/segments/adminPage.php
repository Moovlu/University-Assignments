<div id="adminPage">
    <h2 class="float-left">Welcome <?php echo $_SESSION["username"] ?>!</h2>
    <h2 class="mt-4">Submitted Bookings</h2>
    <table class="table table-hover mt-1">
        <tr>
            <th>PatientID</th>
            <th>Booking date</th>
            <th>9am - 12pm</th>
            <th>12pm - 3pm</th>
            <th>3pm - 6pm</th>
            <th>Booking reason</th>
            <th>Time booking was made</th>
        </tr>
    <?php
    // Open appointments file and write to array
    $fp = fopen('appointments.txt', 'r');
    flock($fp, LOCK_SH);
    while (($data = fgetcsv($fp)) !== false) {
        $arrayAppointments[] = $data;
    }
    // Go through row by row
    for ($i = 1; $i < count($arrayAppointments); $i++) {
        // Convert dates to human readable (day date month year)
        $bookingDate = date("l jS \of F Y", strtotime($arrayAppointments[$i][1]));
        $timeDate = date("l jS \of F Y h:i:s A", strtotime($arrayAppointments[$i][6]));
        // Print table data
        echo '<tr>'.
        '<td>'.$arrayAppointments[$i][0].'</td>'.
        '<td>'.$bookingDate.'</td>'.
        '<td>'.$arrayAppointments[$i][2].'</td>'.
        '<td>'.$arrayAppointments[$i][3].'</td>'.
        '<td>'.$arrayAppointments[$i][4].'</td>'.
        '<td>'.$arrayAppointments[$i][5].'</td>'.
        '<td>'.$timeDate.'</td>'.'</tr>';
    }
    ?>
    </table>

    <h2>Add New Login</h2>
    <div id="addLoginForm">
        <form method="post" name="addloginForm" class="leftAddUser">
            <div class="form-group">
                <label for=username" class="mt-1">Username</label>
                <input type="username" class="form-control mt-1" placeholder="Enter new username" name="newUsernameInput">
            </div>
            <div class="form-group">
                <label for="password" class="mt-4">Password</label>
                <input type="password" class="form-control mt-1" placeholder="Enter new password" name="newPasswordInput">
            </div>
            <div>
                <button type="submit" class="btn btn-primary mt-4" name="submitNewUser">Create new login</button>
            </div>
        </form>
        <p><?php echo $addLoginMessage ?></p>
    </div>





    <form method="post" name="logout" class="text-center">
    <button type="submit" class="btn btn-info mt-4 float-left mb-4" name="logout">Logout</button>
    </form>
</div>