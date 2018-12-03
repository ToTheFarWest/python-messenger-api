from flask import request, abort, json
from flask_api import FlaskAPI
import uuid
from users import users

app = FlaskAPI(__name__)

@app.route('/')
def hello_world():
  return "Hello, world!"

@app.route('/register', methods = ['POST'])
def register_user():
  if not request.json:
    abort(400)
  for u in users:
    if u['username'] == request.json['username']:
      return{'error': 'User already exists!'}
  else:
    user = request.json
    user['id'] = uuid.uuid4()
    user['token'] = uuid.uuid4()
    users.append(user)
  return {'response': {'user': user}}

@app.route('/login')
def login():
  username = request.args.get('username')
  password = request.args.get('password')

  for u in users:
    if u['username'] == username and u['password'] == password:
      return{'response': {'token': u['token']}}
    else:
      return{'error': 'Incorrect username or password!'}


@app.errorhandler(400)
def bar(error):
    return {'error': 'Bad request'}, 400
