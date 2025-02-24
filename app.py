from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    return jsonify({"value": random.randint(1, 100)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
