
# Imports
import webbrowser
import html, applogic,user 
from bottle import Bottle, run, request, response, route

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
@app.route('/login', method='GET')
def get_login_page():
    """ This function returns the login page.

    Returns:
        String: The login page.
    """
    return html.RenderEngine().render_login_page()

@app.route('/login', method='POST')
def login_user():
    """ This function verifies the user sign in information.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found. 
    """
    form_data = request.form.todict()
    
    if UserMan.login_user(form_data['username'], form_data['password']):
        response.status_code = 200
        
        """TODO : decide which page to render after login"""
        html.RenderEngine().render_user_page() 
        username = request.forms.get('username') 
        UserMan.get_user_history(username)
    else:
        response.status_code = 404
        
        
"""TODO : Refactor the /user api endpoint to show user info?"""
"""@app.route('/user', method='GET')
def verify_user():
    "" This function verifies the user sign in information.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found. 
    ""
    form_data = request.form.todict()
    
    if UserMan.login_user(form_data['username'], form_data['password']):
        response.status_code = 200
        html.RenderEngine().render_login_page()
        username = request.forms.get('username') 
        UserMan.get_user_history(username)
    else:
        response.status_code = 404
"""

@app.route('/update_user/<username>', method='POST')
def update_user_info(username):
    """ This function updates the user information if the user exists
        or creates a new user if the user does not exist.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found.
    """
    if UserMan.update_user_password(username, request.forms.get('new_password')):
        response.status_code = 200
    else:
        response.status_code = 404
    
@app.route('/register_user', method='GET')
def get_register_user():
    """ This function returns the register user page.

    Returns:
        String: The register user page.
    """
    
    return html.RenderEngine().render_signup_page()

@app.route('/register_user', method='POST')
def register_user():
    """ This function registers a new user to the server.

    Returns:
        Int: 400 if there is an issue, 200 if the user is created.
    """
    
    if UserMan.register_user(request.forms.get('username'), request.forms.get('password')):
        response.status_code = 200
        html.render_main_game_page()
    else:
        response.status_code = 400
        return "User already exists"

# Routes for handling game information
@app.route('/create_game/<user_id1>/<user_id2>', method='POST')
def create_game(user_id1,user_id2):
    """ This function creates a new game and returns the game's page.

    Returns:
        String: The game's page.
    """
    game_id = UserMan.gen_game_id(user_id1,user_id2)
    Game.create_game(game_id)
    return html.RenderEngine().render_main_game_page(Game.get_board())

@app.route('/check_game/<game_id>/<x>/<y>')
def check_game_state(game_id, x, y):
    """ This function checks the game state of the given ID and returns the updated HTML.

    Returns:
        the new board state in HTML.
    """
    
    if Game.make_move(game_id,x,y):
        response.status_code = 200
        return html.RenderEngine().render_board(Game.get_board())
    else :
        response.status_code = 400
        return "Invalid Move"
    

@app.route('/save_game/<game_id>', method='POST')
def save_game_state(game_id):
    """ This function updates the game state of the given ID.

    Returns:
        Int: 400 if there was an error, 200 if the game is found.
    """
    if Game.save_board(game_id):
        response.status_code = 200
        return "Game Saved"
    else :
        response.status_code = 400
        

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
    webbrowser.open('http://localhost:8080/')
