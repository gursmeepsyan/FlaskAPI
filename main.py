from flask import Flask 
from flask_restful import Resource , Api

app = Flask("VideoAPI")
api = Api(app)

videos = {
    'video1': { 'title': "I am 1"},
    'video2': { 'title': "I am 2"}

}

class Video(Resource):

    def get(self):
        return videos

api.add_resource(Video,'/') 



if __name__ == "__main__":
    app.run(debug=True)