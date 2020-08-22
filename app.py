import os
from flask import Flask, abort, jsonify, request

from models import setup_db, Question, Answer

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)

    @app.route('/')
    def index():
        return "not yet implemented"
    
    @app.route('/question/<int:question_id>')
    def get_question(question_id):
        question = Question.query.filter(Question.id == question_id).one_or_none()

        if question is None:
            abort(404)
        
        return jsonify({
            'success': True,
            'question': question.format()
        })
    
    # @app.route('/question' methods=['POST'])
    # def add_question():
    #     data = request.get_json()
    #     question_text = data.get('questionText', None)

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)