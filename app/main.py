from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/ping')
def ping():
    if request.method == 'GET':
        print('200')
        return Response(status=200)

@app.route('/')
def home():
    return 'Im here'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
