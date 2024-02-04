# import the modules flask (main class) request and jsonify are used for handling HTTP requests and generating JSON responses
# from flask import Flask, request, jsonify
# create a flask app - The '__name__' is used to determine the root
# app = Flask(__name__)

# This is a decorator in Python that is used to bind a function to a URL route. 
# In this case, the home function is associated with the root URL ("/"). 
# So, when a user accesses the root URL of the web application, the home function will be called.
# @app.route("/")
#This function, named home, is the handler for the specified route ("/"). 
# It doesn't take any parameters. When a user accesses the root URL, this function will be executed.
# def home():
#       return "Home"
#return "Home": The function returns the string "Home". In the context of a web application, 
# this string will be sent as the response to the user's browser when they access the root URL

# a path parameter is a variable part of a URL path that is used to capture and extract values from the URL. 
# Path parameters are specified within the route pattern and are used to define dynamic parts of the URL, 
# allowing the same route handler to handle different inputs.

#http://127.0.0.1:5000/get-user/123?extra=%22hello%22
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#       user_data = {
#             "user_id": user_id,
#             "name": "John Doe",
#             "email": "john.doe@example.com",
#       }
      
#       extra = request.args.get("extra")
#       if extra:
#             user_data["extra"] = extra
            
#       return jsonify(user_data), 200

# The if __name__ == '__main__': block checks whether the script is being run directly (not imported as a module). If it is the main script being executed, the app.run(debug=True) line starts the Flask development server with debugging enabled.
# if __name__ == '__main__':
#       app.run(debug=True)
      

# Methods we can use:
#       GET - request data from a specified source
#       POST - create a resource
#       PUT - update a resource
#       DELETE - delete a resource


# Note: Running a Flask application with debug=True in a production environment is not recommended, 
# as it can expose sensitive information and security vulnerabilities. In production, 
# it's advisable to set debug=False and deploy using a production-ready 
# server, such as Gunicorn or uWSGI, in conjunction with a reverse proxy like Nginx or Apache.

# ---------------------------------------------
# GET Root

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# #http://127.0.0.1:5000/get-user/123?extra=%22hello%22
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#       user_data = {
#             "user_id": user_id,
#             "name": "John Doe",
#             "email": "john.doe@example.com",
#       }
      
#       extra = request.args.get("extra")
#       if extra:
#             user_data["extra"] = extra
            
#       return jsonify(user_data), 200

# if __name__ == '__main__':
#       app.run(debug=True)
      
# ---------------------------------------------
# POST Root

from flask import Flask, request, jsonify

app = Flask(__name__)

#http://127.0.0.1:5000/get-user/123?extra=%22hello%22
@app.route("/get-user/<user_id>")
def get_user(user_id):
      user_data = {
            "user_id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com",
      }
      
      extra = request.args.get("extra")
      if extra:
            user_data["extra"] = extra
            
      return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
      data = request.get_json("data")
      
      return jsonify(data), 201

if __name__ == '__main__':
      app.run(debug=True)