
# Imports
import webbrowser
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
def get_game_page():
    """ This function returns the game's page.

    Returns:
        String: The game's page.
    """
    pass

# Routes for handling user information and authentication
@app.route('/user')
def verify_user():
    """ This function verifies the user sign in information.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found. 
    """
    pass

@app.route('/update_user/<user_id>', method='POST')
def update_user_info():
    """ This function updates the user information if the user exists
        or creates a new user if the user does not exist.

    Returns:
        Int: 404 if the user is not found, 200 if the user is found.
    """
    pass

# Routes for handling game information
@app.route('/check_game/<game_id>')
def get_game_state():
    """ This function returns the game state of the given ID in a 9x9 Matrix.

    Returns:
        Array: Returns the game state in a matrix.
    """
    
    pass

@app.route('/save_game/<game_id>', method='POST')
def save_game_state():
    """ This function updates the game state of the given ID.

    Returns:
        Int: 404 if the game is not found, 200 if the game is found.
    """
    pass


#Starts the server and opens the web browser
if __name__ == '__main__':
    run(app, host='localhost', port=8080)
    webbrowser.open('http://localhost:8080')