# Open-OAuth

This small python project was created to implement an OAuth v1.0a provider.

It will authenticate any user, so please do not use this outside of testing. Depending on the web app / API you wish to emulate, you may need to add additional endpoints and return the expected data.

## Usage

From a console
`
$ python3 ./oauth_server.py
`

A server will begin running on all interfaces on port 8081. 

The OAuth specifications have the following requests made:

1. Client makes a request to /oauth/request_token
2. Server responds back with a unique oauth_token and secret
3. Client makes a request to /oauth/authorize with the oauth_token
4. Server will authenticate the user. This server will automatically authenticate a user, so long as the oauth_token is known. The server will reach out to the callback url specified as a parameter in 1.
5. Client makes a request to /oauth/access_token
6. Server responds with the oauth_token and secret
7. Client may proceed with using the application

This process is best explained through [https://oauthbible.com/#oauth-10a-three-legged](https://oauthbible.com/#oauth-10a-three-legged) and [https://oauth.net/core/1.0a/](https://oauth.net/core/1.0a/)
