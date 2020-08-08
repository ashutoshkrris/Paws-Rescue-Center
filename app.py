"""Flask Application for Paws Rescue Center."""
from flask import Flask
app = Flask(__name__)

"""1. Add a View Function for the Home page."""
@app.route('/')
def home():
    return '<h1><center>Paws Rescue Center 🐾</center></h1>'

"""2. Add a View Function for the About page."""
@app.route('/about')
def about():
    return """<h1><center>About Us:</center></h1><p>We are a non-profit organization working as an animal rescue.
    We aim to help you connect with purrfect furbaby for you!
    The animals you find at our website are rescued and rehabilitated animals.
    Our mission is to promote the ideology of "Adopt, don't Shop"!</p>
    """

if __name__ == "__main__":
    """ """
    app.run(debug=True)