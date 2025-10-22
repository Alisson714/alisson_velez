from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/add', methods=['GET'])
def add_endpoint():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = add(a, b)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400

@app.route('/')
def home():
    return '''
    <h1>Calculator API</h1>
    <p>Use GET /add?a=2&b=3 to add two numbers</p>
    <p>Example: <a href="/add?a=2&b=3">/add?a=2&b=3</a></p>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)