from flask import Flask, request
import logging
import json
from googletrans import LANGUAGES
from googletrans import Translator

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/post', methods=['POST'])
def main():

    logging.info('Request: %r', request.json)

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(response, request.json)

    logging.info('Request: %r', response)

    return json.dumps(response)


def handle_dialog(res, req):

    user_id = req['session']['user_id']

    if req['session']['new']:

        res['response']['text'] = "Привет! Я могу переводить слова! Начинай диалог с 'Переведи слово'."

        return
    if 'переведи слово' in req['request']['original_utterance'].lower():
        word = get_word(req)
        res['response']['text'] = translator(word)
    else:
        res['response']['text'] = 'Не поняла!'
    return


def translator(word):
    tr = Translator()
    word = tr.translate(word, dest='ru').text
    return word


def get_word(req):
    text = req['request']['original_utterance'].lower().replace('переведи слово', '')
    return text


if __name__ == '__main__':
    app.run()
