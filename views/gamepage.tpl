<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team G - Ultimate Tic Tac Toe</title>
    <link rel="stylesheet" type="text/css" href="../static/gamepage.css">
</head>
<body>

    <div class="info-container">
        <h1 class="h1-label">Current Player</h1>

        <!-- This is temporary Dummy text- This will be replaced with dynamic usernames -->
        <h1 class="h1-output">Player1Username</h1> 

        <h1 class="h1-label">Opponent Username</h1>

        <!-- This is temporary Dummy text- This will be replaced with dynamic usernames -->
        <h1 class="h1-output">Player2Username</h1>

        <h1 class="h1-label">Turn</h1>

        <h1 class="h1-output">It's your turn!</h1>

    </div>

    <div class="board-container">

        <h1>Ultimate Tic Tac Toe Game Team G</h1>
        <h1>Game Board</h1>
    
        <table class="board">
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="0,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="0,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="1,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="1,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="2,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="2,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="3,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="3,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="4,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="4,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="5,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="5,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="6,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="6,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="7,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="7,8"></button></td>
                </form>
            </tr>
            <tr>
                <form action="/click" method="post">
                    <td class="cell"><button type="submit" name="coordinate" value="8,0"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,1"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,2"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,3"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,4"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,5"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,6"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,7"></button></td>
                    <td class="cell"><button type="submit" name="coordinate" value="8,8"></button></td>
                </form>
            </tr>
        </table>

    </div>

    <div class="score-container">
        
        <h1 class="h1-label">Your Score</h1>

        <!-- This is temporary Dummy text- This will be replaced with dynamic scores -->
        <h1 class="h1-output">2 (3x3) boards won</h1>

        <h1 class="h1-label">Opponents Score</h1>

        <!-- This is temporary Dummy text- This will be replaced with dynamic scores -->
        <h1 class="h1-output">4 (3x3) boards won</h1>

        <h1 class="h1-label">Result</h1>

        <!-- This is temporary Dummy text- This will be replaced with dynamic result -->
        <h1 class="h1-output">The Game is a tie!</h1>

    </div>

</body>
</html>