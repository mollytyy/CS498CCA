from flask import Flask, request
app = Flask(__name__)

seed = 0
d = {}


@app.route('/', methods=['POST', 'GET'])
def main():
    global seed
    if request.method == 'POST':
        new_seed = request.get_json()
        seed = new_seed["num"]
        d['num'] = new_seed["num"]
        return d['num']
    else:
        d['num'] = seed
        return d['num']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
