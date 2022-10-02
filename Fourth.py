from Flask import flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hallo world!'
app.run(port=8000)