from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send():
    try:
        content = request.json
        f = open('text.txt', 'w')
        f.write(str(content))
        f.close()
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'error'})


@app.route('/update', methods=['GET'])
def send2():
    try:
        f = open('text.txt', 'r')
        chat = eval(f.read())
        f.close()
    except:
        chat={}
        f = open('text.txt', 'w')
        f.write(str(chat))
        f.close()
    return jsonify(chat)


if __name__ == 'ls__main__':
    app.run()
