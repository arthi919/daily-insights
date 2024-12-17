rom flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Daily Insights!'

@app.route('/api/hello')
def api_hello():
    return {'message': 'Hello from the API!'}
