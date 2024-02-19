from subprocess import call
import requests
import hashlib
import json

domain = 'YOUR-DOMAIN-HERE'

uuid = hashlib.md5(domain.encode('utf-8')).hexdigest()

result = requests.get('http://' + domain)

ssl_result = requests.get('https://' + domain).status_code

uses_ssl = (ssl_result == 200)

uses_css = (result.text.find('<link rel="stylesheet"') > -1)

uses_js = (result.text.find('<script language="JavaScript"') > -1)

profile = { 'uuid': uuid,'ssl_result': ssl_result, 'name': domain ,'uses_ssl': uses_ssl, 'uses_css': uses_css, 'uses_js': uses_js}

print(json.dumps(profile))