# Import Flask
from flask import Flask

# Create a new flask instance
app = Flask(__name__)

# Create the Flask route
@app.route('/')
def hello_world():
	return 'Hello world'