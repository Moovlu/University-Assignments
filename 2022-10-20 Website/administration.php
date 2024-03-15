<?php
    $pageName = 'Administration';
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
            <h1 class="text-center mt-4">Administration Area</h1>
            <p class="text-center text-muted">This place is reserved for employees of Russel Street Medical only</p>
    
<?php
if (!isset($_SESSION['username'])||isset($_POST["logout"])) {
    echo '
    <div id="loginForm">
        <form method="post" name="adminForm" class="centerLogin">
            <div class="form-group">
                <label for=username" class="mt-4">Username</label>
                <input type="username" class="form-control mt-1" placeholder="Enter username" name="usernameInput">
            </div>
            <div class="form-group">
                <label for="password" class="mt-4">Password</label>
                <input type="password" class="form-control mt-1" placeholder="Enter password" name="passwordInput">
            </div>
            <div class="text-center">
                <button type="submit" class="btn btn-primary mt-4" name="submitLogin">Submit</button>
            </div>
        </form>
        <p class="text-center">'.$loginMessage.'</p>
    </div>';
}
if (isset($_SESSION['username'])) {
    include("segments/adminPage.php");
}
?>
        </main>