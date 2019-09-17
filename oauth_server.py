from flask import Flask
from flask import request
from flask import Response
from urllib.parse import urlencode
from urllib.parse import unquote
import requests
import random
import string

app = Flask(__name__)


tokens = []
RANDOM_CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits

@app.route('/', methods=['GET'])
def status_message():
    return jsonify({'Status' : 'Up and running'})

@app.route('/oauth/request_token', methods=['POST'])
def requestToken():
  oauth_header = request.headers['Authorization']
  oauth_params = oauth_header.split("OAuth ")[-1].split(", ")

  oauth_data = {}
  for param in oauth_params:
    name, value = param.split("=")
    value = value.replace('"', '')

    if name == 'oauth_callback':
      value = unquote(value)
    oauth_data[name] = value

  # Generate oauth token and secret
  response = {}
  response['oauth_token'] = ''.join(random.choice(RANDOM_CHARSET) for i in range(random.randint(40,50)))
  response['oauth_token_secret'] = ''.join(random.choice(RANDOM_CHARSET) for i in range(random.randint(40,50)))
  response['oauth_callback_confirmed'] = "true"

  token = {'oauth_token': response['oauth_token'], 'oauth_token_secret': response['oauth_token_secret'], 'callback_url': oauth_data['oauth_callback']}
  print(token)
  tokens.append(token)

  # Send request back to callback with token
  requests.get(token['callback_url'] + "?oauth_token=" + response['oauth_token'])

  return Response(urlencode(response), mimetype='application/x-www-form-urlencoded')

if __name__ == "__main__":
    app.run(debug=True)