from bottle import Bottle, run, request, response, route, static_file, template


app = Bottle()





if __name__ == '__main__':
    run(app, host='localhost', port=8080)