from run import db
from flask import jsonify


class Post(db.Model):

    # schema
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    # save the information that was filled
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        allPost = cls.query.all()
        array = []
        for item in allPost:
            post = item.__dict__
            array.append(
                {"id": post["id"], "topic": post["topic"], "content": post["content"]}
            )
        return array

    @classmethod
    def find_by_topic(cls, topic):
        return cls.query.filter_by(topic=topic).first()

    @classmethod
    def put(cls, topic):
        cls.query.filter_by(topic=topic).update({"content": "random message"})
        db.session.commit()
        return {"message": "Topic {} was updated".format(topic)}

    @classmethod
    def delete(cls, topic):
        cls.query.filter_by(topic=topic).delete()
        db.session.commit()
        return {"message": "Topic {} was deleted".format(topic)}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {"message": "{} row(s) deleted".format(num_rows_deleted)}
        except:
            return {"message": "Something went wrong"}
