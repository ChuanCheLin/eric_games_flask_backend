from flask import Flask, request, jsonify
from mirrorMazeSolver import generate_puzzle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/generate_puzzle', methods=['GET'])
def generate():
    # Extract query parameters for height and width, with defaults
    height = request.args.get('height', default=5, type=int)
    width = request.args.get('width', default=5, type=int)

    puzzle_data = generate_puzzle(height, width)
    return jsonify(puzzle_data)


if __name__ == '__main__':
    app.run(debug=True)
