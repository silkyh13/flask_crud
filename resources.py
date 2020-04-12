from flask_restful import Resource, reqparse
from models import Post

parser = reqparse.RequestParser()
parser.add_argument("topic", help="This field cannot be blank", required=True)
parser.add_argument("content", help="This field cannot be blank", required=True)


class AddPost(Resource):
    def post(self):
        data = parser.parse_args()

        if Post.find_by_topic(data["topic"]):
            return {"message": "Topic {} already exists".format(data["topic"])}

        # creates new entry
        new_topic = Post(topic=data["topic"], content=data["content"])

        try:
            new_topic.save_to_db()
            return {"message": "Topic {} was created".format(data["topic"])}
        except:
            return {"message": "Something went wrong"}, 500


# update one entry
class Put(Resource):
    def put(self, topic):
        # print(Post.find_by_topic(topic).__dict__["topic"], "made it here")
        return Post.put(topic)


# get all entries
class GetAll(Resource):
    def get(self):
        posts = Post.get_all()
        return posts


class Delete(Resource):
    def delete(self, topic):
        return Post.delete(topic)


class DeleteAll(Resource):
    def delete(self):
        return Post.delete_all()
