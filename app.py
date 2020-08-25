import os, uuid
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from models import setup_db, Question, Answer

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Content-Type,Authorization,true"
            )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET,PUT,POST,DELETE,PATCH,OPTIONS"
            )
        return response

    @app.route('/')
    def index():
        return "not yet implemented"
    
    @app.route('/questions/<int:question_id>')
    def get_question(question_id):
        question = Question.query.filter(Question.id == question_id).one_or_none()

        if question is None:
            abort(404)
        
        return jsonify({
            'success': True,
            'question': question.format()
        })
    
    @app.route('/questions', methods=['POST'])
    def add_question():
        data = request.get_json()
        question_text = data.get('questionText', None)
        answers = data.get('answers', None)
        print(f"Answers in request data: {answers}")
        try:
            new_question = Question(
                text=question_text,
                uuid=str(uuid.uuid4().hex)
            )
            new_question.insert()

            for answer_text in answers:
                print(f"\tcreating answer with text {answer_text}")
                Answer(
                    text=answer_text,
                    question_uuid=new_question.uuid,
                    uuid=str(uuid.uuid4().hex)
                ).insert()
        
        except Exception as e:
            print(f"Exception {e} in add_question()")
            abort(422)

        print(f"Successfully added {new_question}")
        return jsonify({
            'success': True,
            'uuid': new_question.uuid
        })
    
    @app.route('/answers/<int:answer_id>', methods=['GET', 'POST'])
    def get_answer(answer_id):
        answer = Answer.query.filter(Answer.id==answer_id).one_or_none()

        if answer is None:
            abort(404)
            
        if request.method == 'POST':
            answer.increment_count()
    
        return jsonify({
                "success": True,
                "answer": answer.format()
            })

    return app

app = create_app()

@app.errorhandler(404)
def not_found(error):
    print(f"404 Error: {error}")
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)