from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
# database+driver:/user:password@localhost:port#/databaseName
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqlconnector://root:JackAndKat@127.0.0.1:3306/blog"
db = SQLAlchemy(app)

# A list of functions that will be called at the beginning of the first request to this instance. To register a function, use the
@app.before_first_request
def create_tables():
    db.create_all()


import models, resources

api.add_resource(resources.AddPost, "/post")
api.add_resource(resources.GetAll, "/find")
api.add_resource(resources.DeleteAll, "/delete")
api.add_resource(resources.Delete, "/delete/<topic>")
api.add_resource(resources.Put, "/put")

api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)
