from logging import debug
from re import M
from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
        {
            'Contact': u'9987644456',
            'Name': u'Raju',
            'done': 'false',
            'id': 1
        },
        {
            'Contact': u'9876543222',
            'Name': u'Rahul',
            'done': 'false',
            'id': 2
        }
]

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/getdata')
def gettask():
    return jsonify({
        'data': tasks
    })

@app.route('/adddata', methods = ['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'status': 'error', 
            'message': 'Please provide the data'
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        'status': 'success',
        'message': 'Task added successfuly'
    })

if(__name__=='__main__'):
    app.run(debug=True)