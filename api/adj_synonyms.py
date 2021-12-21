from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):

    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if 'word' in dic:
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
        r = requests.get(url + dic['word'])
        data = r.json()
        parts_of_speech = []
        synonyms = []
        for word_data in data:
            part_of_speech = word_data['meanings'][0]['partOfSpeech']
            if part_of_speech == 'adjective':
                synonyms = word_data['meanings'][0]['definitions'][0]['synonyms']
            else:
                message = [f'{dic["word"]} is not an adjective']
            
        if len(synonyms):
            message = str(synonyms)

    else:
        # TODO: should send a status 400, only adjectives should be allowed
        message = 'No word given'


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return