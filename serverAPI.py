
# Imports
import webbrowser
from bottle import Bottle, run, request, response, route
import html, applogic,user 
#Create the bottle app
app = Bottle()

# Routes for loading pages
@app.route('/')
def get_homepage():
    """ This function returns the homepage of the server.

    Returns:
        String: The homepage of the server.
    """
    return "Hello World!"


@app.route('/game/<game_id>')
def get_game_page(game_id):
    """ This function returns the game's page.

    Returns:
        String: The game's page.
    """
    return html.RenderEngine().render_main_game_page(Game.get_board(game_id))

# Routes for handling user information and authentication
@app.route('/user')
def verify_user():
    """ This function verifies the user sign in information.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found. 
    """
    if UserMan.login_user(request.forms.get('username'), request.forms.get('password')):
        response.status_code = 200
        html.RenderEngine().render_login_page()
        username = request.forms.get('username') 
        UserMan.get_user_history(username)
    else:
        response.status_code = 404

@app.route('/update_user/<user_id>', method='POST')
def update_user_info():
    """ This function updates the user information if the user exists
        or creates a new user if the user does not exist.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found.
    """
    

# Routes for handling game information
@app.route('/check_game/<game_id>/<x>/<y>')
def check_game_state(game_id, x, y):
    """ This function checks the game state of the given ID and returns the updated HTML.

    HTML Example: 
    '''
        <a href="/check_game/game_id/x/y>Press me</a>
    '''
    Returns:
        Array: Returns the game state in a matrix.
    """
    
    if Game.make_move(game_id,x,y):
        response.status_code = 200
        return html.RenderEngine().render_board(Game.get_board())
    else :
        response.status_code = 404
        return "Invalid Move"
    

@app.route('/save_game/<game_id>', method='POST')
def save_game_state(game_id):
    """ This function updates the game state of the given ID.

    Returns:
        Int: 404 if the game is not found, 200 if the game is found.
    """
    if Game.save_board(game_id):
        response.status_code = 200
        return "Game Saved"
    else :
        response.status_code = 404
        

@app.route('/load_game/<game_id>')
def load_game_state(game_id):
    """ This function loads the game state of the given ID.

    Returns:
        Array: Returns the game state in a matrix.
    """
    if Game.load_board(game_id):
        response.status_code = 200
        return html.RenderEngine().render_board(Game.get_board())
    else :
        response.status_code = 404
        return "Game Not Found"


#Starts the server and opens the web browser
if __name__ == '__main__':
    Game = applogic.SuperTicTacToe()
    UserMan = user.UserManager()
    run(app, host='localhost', port=8080)
    webbrowser.open('http://localhost:8080')
