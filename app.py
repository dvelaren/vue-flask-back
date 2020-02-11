from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS = [{'user': 'David', 'title': 'Administrator'},
         {'user': 'Esteban', 'title': 'Brother'},
         {'user': 'Julian', 'title': 'Developer'}
        ]

@app.route('/api/v1/consult')
def consult():
    return jsonify(USERS)

if __name__ == '__main__':
    app.run(debug=True)