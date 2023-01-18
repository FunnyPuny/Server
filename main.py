from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/ping', method='GET')
def ping():
    if request.method == 'GET':
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
