from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

BOOKS = [
    {
        'title': ['Data mining para dummies',
                  'Salvando mi tierra',
                  'Comunismo despatriado'],
        'correct_title': 'El estrés que me carcome',
        'author': 'Camilo Torres',
        'paperback': True
    },
    {
        'title': ['Agriculture 4.0: Machine Learning',
                  'Anomaly detection for Industry 4.0',
                  'Visual Analytics in Wastewater Management'],
        'correct_title': 'I love DISH//',
        'author': 'David Velásquez',
        'paperback': False    
    },
    {
        'title': ['Quantum AI',
                  'Rapidminer for industrials',
                  'Creating value from statistics'],
        'correct_title': 'Joder... eso es!',
        'author': 'Aitor Moreno',
        'paperback': True
    }
]

@app.route('/books', methods=['GET'])
def books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

if __name__ == '__main__':
    app.run(debug=True)
