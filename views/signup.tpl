<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team G - Ultimate Tic Tac Toe</title>
    <link rel="stylesheet" href="../static/signup.css">
</head>
<body>

    <h1 class="display-header">Ultimate Tic Tac Toe Game Team G</h1>
    <form class="form-container" action="/register_user" method="post">
        <span class="form-title">Player Registration</span>
        <input type="text" id="username" name="username" placeholder="Username">
        <input type="password" id="password" name="password" placeholder="Password">
        <div class="btn-div">
            <button class="register-submit">Register</button>
        </div>
        <div class="login-div">
            <p>Already have an account? <a href="/login">Login</a></p>
        </div>
    </form>

</body>
</html>