import redis
import flask

r = redis.Redis(host = 'localhost', port = '6379', db = 0)

app = flask.Flask(__name__)

@app.route('/')
def home():
    reply = {'data':'Redis API'}
    return flask.jsonify(reply) 

@app.route('/get', methods = ['GET'])
def get():
    key = flask.request.args.get('key')
    data = 'not found'
    if r.exists(key):
        data = r.get(key).decode()
    reply = {'data':data}
    return flask.jsonify(reply)

@app.route('/post', methods = ['POST'])
def post():
    data = flask.request.get_json()
    status = r.set(data['key'], data['value'])
    reply = {'status':status}
    return flask.jsonify(reply)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)