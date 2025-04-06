from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (or you can specify specific origins)

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')
    except TypeError:
        return jsonify({"error": "Missing or invalid parameters"}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
