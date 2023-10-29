import uuid

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import weaviate

app = Flask(__name__)
api = Api(app, version='1.0', title='Weaviate API', description='A simple Weaviate API with Swagger')

client = weaviate.Client("http://31.220.108.226:8080")

ns = api.namespace('api', description='API operations')

session_model = api.model('Session', {
    'session_name': fields.String(required=True, description='Session name'),
})

get_session_model = api.model('Session', {
    'session_name': fields.String(required=True, description='Session name'),
})

file_model = api.model('File', {
    'session_name': fields.String(required=True, description='Session name'),
    'text_content': fields.String(required=True, description='Text content')
})

question_model = api.model('Question', {
    'session_name': fields.String(required=True, description='Session name'),
    'question': fields.String(required=True, description='Question text'),
})


@ns.route('/CreateSession')
class CreateSessionResource(Resource):
    @ns.expect(session_model)
    @ns.response(201, 'Session created successfully')
    def post(self):
        data = request.get_json()
        session_name = data.get('session_name').capitalize()
        print(session_name)
        # Define schema for your session
        schema = {
            "classes": [
                {
                    "class": session_name,
                    "properties": [
                        {
                            "name": "fileText",
                            "dataType": ["text"]
                        }
                    ]
                }
            ]
        }

        exists = client.schema.exists(session_name)
        if exists:
            return f"Your session {session_name} already exists!"

        client.schema.create(schema)
        return f"Your session {session_name} now exists!"


@ns.route('/UploadFile')
class UploadFileResource(Resource):
    @ns.expect(file_model)
    @ns.response(201, 'File uploaded successfully')
    def post(self):
        data = request.get_json()
        session_name = data.get('session_name').capitalize()
        text_content = data.get('text_content')

        # Create a data object in the specified session
        data_object = {
            "fileText": text_content,
            "session_id": data.get('session_id')
        }

        new_uuid = uuid.uuid1()
        client.data_object.create(data_object, class_name=session_name, uuid=new_uuid)
        if client.data_object.exists(new_uuid):
            return f"Your object was uploaded with uuid {new_uuid}"
        return "There was an error uploading your object."


@ns.route('/PostSession')
class GetSessionResource(Resource):
    @ns.expect(get_session_model)
    @ns.response(200, 'Session data retrieved successfully')
    def post(self):
        data = request.get_json()
        session_name = data.get('session_name').capitalize()

        query = (
            client.query.get(session_name, "fileText").with_limit(3)
        )
        result = query.do()

        return result


@ns.route('/AskQuestion')
class AskQuestionResource(Resource):
    @ns.expect(question_model)
    @ns.response(200, 'Question asked successfully')
    def post(self):
        data = request.get_json()
        session_name = data.get('session_name').capitalize()
        question = data.get('question')

        # Mock logic to get similar text data
        # In a real scenario, you would use your model to find similar text data
        response = {
            "similar_texts": [
                {"text": "sample text 1", "similarity": 0.98},
                {"text": "sample text 2", "similarity": 0.95},
                {"text": "sample text 3", "similarity": 0.93}
            ]
        }
        return response


if __name__ == '__main__':
    app.run(debug=True)
