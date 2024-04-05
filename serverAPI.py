
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
        redirect: The login page.
    """
    
    return redirect('/login')

@app.route('/resetpassword', method='GET')
def reset_password():
    """ This function returns the reset password page.

    Returns:
        String: The reset password page.
    """
    return frontend.RenderEngine().render_reset_password()

@app.route('/game/<game_id>')
def get_game_page(game_id):
    """ This function returns the game's page.

    Returns:
        String: The game's page.
    """
    if applogic.SuperTicTacToe().load_board(game_id):
        response.status = 200
        return frontend.RenderEngine().render_main_game_page(applogic.SuperTicTacToe().load_board(game_id))
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
    form_data = dict(request.forms)
    
    if UserMan.login_user(form_data['username'], form_data['password']):
        response.status = 200
        
        username = request.forms.get('username')
        
         
        UserMan.get_user_history(username)
        return frontend.FrontEndOps().process_online_players(UserMan.get_all_online_users(),username,UserMan.get_leaderboard(),1,2) 
    else:
        response.status = 404
        return "User not found"

@app.route('/update_user', method='POST')
def update_user_info():
    """ This function updates the user information if the user exists
        or creates a new user if the user does not exist.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found.
    """
    if UserMan.update_user_password(request.forms.get('username'),  request.forms.get('new_password')):
        response.status = 200
        return frontend.FrontEndOps().process_online_players(UserMan.get_all_online_users(),request.forms.get('username'),UserMan.get_leaderboard(),1,2)
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
    form_data = dict(request.forms)
    if UserMan.register_user(request.forms.get('username'), request.forms.get('password')):
        response.status = 200
        active_games = UserMan.get_active_games(form_data['username']) # gets active games for current user, pending frontend implementation
        
        return frontend.FrontEndOps().process_online_players(UserMan.get_all_online_users(),form_data['username'],UserMan.get_leaderboard(),1,2) 
    else:
        response.status = 400
        return "User already exists"

# Routes for handling game information
@app.route('/create_game/<user_id1>/<user_id2>', method=['POST','GET'])
def create_game(user_id1,user_id2):
    """ This function creates a new game and returns the game's page.

    Returns:
        String: The game's page.
    """
    game_id = UserMan.gen_game_id(user_id1,user_id2)
    applogic.SuperTicTacToe().create_game(game_id)
    board,playerturn = applogic.SuperTicTacToe().load_board(game_id)
    return frontend.FrontEndOps().update_board(board,playerturn,user_id1,user_id2,game_id)

@app.route('/check_game', method=['POST','GET'],)
def check_game_state():
    """ This function checks the game state of the given ID and returns the updated frontend.

    Returns:
        the new board state in frontend.
    """
    data = dict(request.forms)
    game_id = data['game_id']
    user_id1 = data['current_user']
    user_id2 = data['opponent']
    x,y = frontend.FrontEndOps().get_cell_coords()
    valid,board,playerturn = applogic.SuperTicTacToe().make_move(game_id,x,y)
    
    if valid:
        response.status = 200
       
        return frontend.FrontEndOps().update_board(board,playerturn,user_id1,user_id2,game_id)
    else :
        response.status = 400
        return "Invalid Move"
    


@app.route('/load_game/<game_id>')
def load_game_state(game_id):
    """ This function loads the game state of the given ID.

    Returns:
        Array: Returns the game state in a matrix.
    """
    data = dict(request.forms)
    user_id1 = data['current_user']
    user_id2 = data['opponent']
    board, playerturn = applogic.SuperTicTacToe().load_board(game_id)
    if isinstance(board, list):
        response.status = 200
        return frontend.FrontEndOps().update_board(board,playerturn,user_id1,user_id2,game_id)
    else :
        response.status = 404
        return "Game Not Found"


#Starts the server and opens the web browser
if __name__ == '__main__':
    UserMan = user.UserManager()
    webbrowser.open('http://localhost:8080/')
    run(app, host='localhost', port=8080)
    
