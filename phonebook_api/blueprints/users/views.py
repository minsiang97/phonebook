from flask import Blueprint, jsonify, request, json
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    return jsonify ([{"id" : user.id, "name" : user.name, "contact_number" : user.contact_number} for user in users])

@users_api_blueprint.route('/', methods=['POST'])
def create():
    name = request.json.get('name')
    contact_number = request.json.get('contact_number')
    user = User(name = name, contact_number = contact_number)

    if user.save():
        return jsonify({"id" : user.id, "name" : user.name, "contact_number" : user.contact_number, "message" : "Successfully posted"})
    else :
        return jsonify({"message" : "Failed to record in database"})
