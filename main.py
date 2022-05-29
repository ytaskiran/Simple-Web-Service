import flask
from flask import request
from hashlib import sha256

app = flask.Flask(__name__)
app.config["DEBUG"] = False

hash_message = {}


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Devpaths HW</h1>
<p>A prototype web service.</p>'''

@app.errorhandler(404)
def message_not_found(e):
    return "<h1>404</h1><p>The message with given hash is not found.</p>", 404

@app.route('/messages', methods=['POST'])
def record_messages():
    if (request.form.get("message") is None):
        return "You did not send a message\n"

    message = request.form.get("message")
    hash_digest = sha256(message.encode('utf-8')).hexdigest()

    if (hash_digest not in hash_message.keys()):
        hash_message[hash_digest] = message


    return hash_digest


@app.route('/messages/<hash>', methods=['GET'])
def hash_to_message(hash):
    if (hash not in hash_message.keys()):
        return message_not_found(404)

    return hash_message[hash]

if __name__ == "__main__":
    app.run()
