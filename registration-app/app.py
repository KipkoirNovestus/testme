from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get data from the request
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    age = data.get('age')
    height = data.get('height')
    gender = data.get('gender')

    # Simulate saving the data to a file or database
    with open('registered_users.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}, Phone: {phone}, Age: {age}, Height: {height}, Gender: {gender}\n")

    # Respond with success
    return jsonify({'message': 'Registration successful!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
