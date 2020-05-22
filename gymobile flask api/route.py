from flask import Flask, request, jsonify,abort,make_response
import pickle
app = Flask(__name__)

#loading sample data from data.py and turn it into <users> (it is a list)
with open('data.pkl', 'rb') as load:
    users = pickle.load(load)

#get route (for all users)
@app.route('/api/users', methods=['GET'])
def users():
    return jsonify({
        'users' : users
    })
    
#get route (for single user)
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#get route (for single user's exercise)
@app.route('/api/user')

#post route
@app.route('/api/user', methods=['POST'])
def create_user():
    if not request.json or not 'Email' in request.json:
        abort(400)
    user = {
        'ID': users[-1]['ID'] + 1,
        'FirstName': request.json['FirstName'],
        'LastName': request.json['LastName'],
        'BMI': request.json['BMI'],
        'Email': request.json['Email'],
        'Rating': request.json['Rating'],
        "Comment": request.json['Comment']
    }
    users.append(user)
    return jsonify({'user': user}), 201

#put route
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['ID'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    user[0]['FirstName'] = request.json.get('FirstName', user[0]['FirstName'])
    user[0]['LastName'] = request.json.get('LastName', user[0]['LastName'])
    user[0]['BMI'] = request.json.get('BMI', user[0]['BMI'])
    user[0]['Email'] = request.json.get('Email', user[0]['Email'])
    user[0]['Comment'] = request.json.get('Comment', user[0]['Comment'])
    return jsonify({'user': user[0]})

#delete route
@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['ID'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})


#error handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#run server (port:5000)
if __name__ == '__main__':

    app.run(debug=True)