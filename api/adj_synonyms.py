from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests as requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):

    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    message = dic

    if 'word' in dic:
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en'
        r = requests.get(url + dic['word'])
        print('word')
        data = r.json
        definitions = []
        for word_data in data:
            print(str(word_data))
            definition = word_data['meanings'][0]['definitions'][0]['definition']
            definitions.append(definition)
        message = str(definitions)

    else:
        # TODO: should send a status 400, only adjectives should be allowed
        message = 'Word must be an adjective'


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return