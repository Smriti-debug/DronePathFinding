from flask import Flask, render_template, request, jsonify
from ai_algorithms import search_path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_path', methods=['POST'])
def find_path():
    data = request.get_json()
    grid = data['grid']
    start = tuple(data['start'])
    goal = tuple(data['goal'])
    algorithm = data['algorithm']

    path = search_path(grid, start, goal, algorithm)
    return jsonify({'path': path})

if __name__ == '__main__':
    app.run(debug=True)
