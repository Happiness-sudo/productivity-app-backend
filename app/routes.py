from flask import request, jsonify
from .models import User, Note
from . import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


def register_routes(app):

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.json

        if User.query.filter_by(username=data['username']).first():
            return jsonify({"error": "Username already exists"}), 400

        user = User(username=data['username'])
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created"}), 201


    @app.route('/login', methods=['POST'])
    def login():
        data = request.json

        user = User.query.filter_by(username=data['username']).first()

        if not user or not user.check_password(data['password']):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=user.id)

        return jsonify({"token": token}), 200

    @app.route('/me', methods=['GET'])
    @jwt_required()
    def get_me():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        return jsonify({
            "id": user.id,
            "username": user.username
        })


    @app.route('/notes', methods=['POST'])
    @jwt_required()
    def create_note():
        user_id = get_jwt_identity()
        data = request.json

        note = Note(
            title=data['title'],
            content=data['content'],
            user_id=user_id
        )

        db.session.add(note)
        db.session.commit()

        return jsonify({"message": "Note created"}), 201


    @app.route('/notes', methods=['GET'])
    @jwt_required()
    def get_notes():
        user_id = get_jwt_identity()

        page = request.args.get('page', 1, type=int)
        notes = Note.query.filter_by(user_id=user_id).paginate(page=page, per_page=5)

        return jsonify([
            {"id": n.id, "title": n.title, "content": n.content}
            for n in notes.items
        ])


    @app.route('/notes/<int:id>', methods=['PATCH'])
    @jwt_required()
    def update_note(id):
        user_id = get_jwt_identity()

        note = Note.query.filter_by(id=id, user_id=user_id).first()

        if not note:
            return jsonify({"error": "Not found"}), 404

        data = request.json

        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)

        db.session.commit()

        return jsonify({"message": "Updated"})

    @app.route('/notes/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_note(id):
        user_id = get_jwt_identity()

        note = Note.query.filter_by(id=id, user_id=user_id).first()

        if not note:
            return jsonify({"error": "Not found"}), 404

        db.session.delete(note)
        db.session.commit()

        return jsonify({"message": "Deleted"})
