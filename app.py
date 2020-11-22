#!/bin/python

import hvac

client = hvac.Client(url='https://localhost:8201', cert=('webApp.pem', 'webAppKey.pem'))
print("is authenticated : {}".format(client.is_authenticated()))
apikey = client.secrets.kv.v2.read_secret_version(path='web_app')
print("password : {}".format(apikey["data"]["data"]["password"]))
