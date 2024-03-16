
# Imports
import webbrowser
import frontend, applogic,user 
from bottle import Bottle, run, request, response, route,redirect
from bottle import static_file

#Create the bottle app
app = Bottle()

@app.route('/static/<filename>')
def server_static(filename):
    """ This function returns the static files from the server.

    Returns:
        String: The static file.
    """
    return static_file(filename, root='./static')

# Routes for loading pages
@app.route('/')
def get_homepage():
    """ This function returns the homepage of the server.

    Returns:
        String: The homepage of the server.
    """
    
    
    return redirect('/login')


@app.route('/game/<game_id>')
def get_game_page(game_id):
    """ This function returns the game's page.

    Returns:
        String: The game's page.
    """
    if applogic.SuperTicTacToe(game_id).load_board(game_id):
        response.status = 200
        return frontend.RenderEngine().render_main_game_page(applogic.SuperTicTacToe(game_id).load_board(game_id))
    else:
        response.status = 404
        return "Game Not Found"


# Routes for handling user information and authentication
@app.route('/login', method='GET')
def get_login_page():
    """ This function returns the login page.

    Returns:
        String: The login page.
    """
    if frontend.RenderEngine().render_login_page():
        response.status = 200
        return frontend.RenderEngine().render_login_page()
    else:
        response.status = 404
        return "Page Not Found"
    

@app.route('/login', method='POST')
def login_user():
    """ This function verifies the user sign in information.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found. 
    """
    form_data = request.form.todict()
    
    if UserMan.login_user(form_data['username'], form_data['password']):
        response.status = 200
        
        """TODO : decide which page to render after login"""
        frontend.RenderEngine().render_user_page() 
        username = request.forms.get('username') 
        UserMan.get_user_history(username)
    else:
        response.status = 404
        return "User not found"


@app.route('/register', method='GET')
def get_registration_page():
    """ This function returns the registration page.

    Returns:
        String: The registration page.
    """
    if frontend.RenderEngine().render_signup_page():
        response.status = 200
        return frontend.RenderEngine().render_signup_page()
    else:
        response.status = 404
        return "Page Not Found"

@app.route('/update_user/<username>', method='POST')
def update_user_info(username):
    """ This function updates the user information if the user exists
        or creates a new user if the user does not exist.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found.
    """
    if UserMan.update_user_password(username, request.forms.get('new_password')):
        response.status = 200
    else:
        response.status = 404
    
@app.route('/register_user', method='GET')
def get_register_user():
    """ This function returns the register user page.

    Returns:
        String: The register user page.
    """
    signup_page = frontend.RenderEngine().render_signup_page()
    if signup_page:
        response.status = 200
        return signup_page
    else:
        response.status = 404
        return "Page Not Found"

@app.route('/register_user', method='POST')
def register_user():
    """ This function registers a new user to the server.

    Returns:
        Int: 400 if there is an issue, 200 if the user is created.
    """
    
    if UserMan.register_user(request.forms.get('username'), request.forms.get('password')):
        response.status = 200
        frontend.RenderEngine().render_main_game_page()
    else:
        response.status = 400
        return "User already exists"

# Routes for handling game information
@app.route('/create_game/<user_id1>/<user_id2>', method='POST')
def create_game(user_id1,user_id2):
    """ This function creates a new game and returns the game's page.

    Returns:
        String: The game's page.
    """
    game_id = UserMan.gen_game_id(user_id1,user_id2)
    applogic.SuperTicTacToe(game_id).create_game(game_id)
    return frontend.RenderEngine().render_main_game_page(applogic.SuperTicTacToe(game_id).load_board())

@app.route('/check_game/<game_id>/<x>/<y>')
def check_game_state(game_id, x, y):
    """ This function checks the game state of the given ID and returns the updated frontend.

    Returns:
        the new board state in frontend.
    """
    
    if applogic.SuperTicTacToe(game_id).make_move(game_id,x,y):
        response.status = 200
        return frontend.RenderEngine().render_updated_board(applogic.SuperTicTacToe(game_id).load_board())
    else :
        response.status = 400
        return "Invalid Move"
    

@app.route('/save_game/<game_id>', method='POST')
def save_game_state(game_id):
    """ This function updates the game state of the given ID.

    Returns:
        Int: 400 if there was an error, 200 if the game is found.
    """
    if applogic.SuperTicTacToe(game_id).save_board(game_id):
        response.status = 200
        return "Game Saved"
    else :
        response.status = 400
        

@app.route('/load_game/<game_id>')
def load_game_state(game_id):
    """ This function loads the game state of the given ID.

    Returns:
        Array: Returns the game state in a matrix.
    """
    if applogic.SuperTicTacToe(game_id).load_board(game_id):
        response.status = 200
        return frontend.RenderEngine().render_updated_board(applogic.SuperTicTacToe(game_id).load_board())
    else :
        response.status = 404
        return "Game Not Found"


#Starts the server and opens the web browser
if __name__ == '__main__':
    UserMan = user.UserManager()
    run(app, host='localhost', port=8080)
    webbrowser.open('http://localhost:8080/')
