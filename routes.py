from flask import Blueprint, render_template, request, jsonify
from controllers.say_hi_controller import say_hi_controller

routes_blueprint = Blueprint('routes_blueprint', __name__)

@routes_blueprint.route('/say-hi', methods=['GET'])
def say_hi_route():
    name = request.args.get('name', 'World')
    greeting = say_hi_controller.say_hi(name)
    return render_template('say_hi.html', greeting=greeting)

@routes_blueprint.route('/api/say-hi', methods=['GET'])
def api_say_hi_route():
    name = request.args.get('name', 'World')
    greeting = say_hi_controller.say_hi(name)
    return jsonify({'greeting': greeting})