from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/translate", methods=['POST'])
def translate():
    # Example for GET: http://127.0.0.1:5000/translate?lang=de-en&text=Weihnachten
    # Example for POST: http://127.0.0.1:5000/translate
    uri = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
    api_key = ""
    key = "key=" + api_key
    text = "&text="
    lang = "&lang="
    format = "&format=plain"

    # Access POSTed JSON
    arg_lang = request.json['lang']
    arg_text = request.json['text']

    yandex_req = uri + key + text + arg_text[0] + lang + arg_lang + format

    print("yandex req:", yandex_req)

    req = requests.get(yandex_req)
    print(req.json())

    return jsonify(req.json())


if __name__ == "__main__":
    app.run()
