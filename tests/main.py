import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

from models import User, Post

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify(post.to_dict())
    return jsonify({"error": "Post not found"}), 404

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    post = Post(
        title=data["title"],
        content=data["content"],
        author_id=data["author_id"]
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)