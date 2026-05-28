from flask import Blueprint, jsonify, request
from app.services import task_service

task_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')

@task_bp.route('/', methods=["POST"])
def create_task():
    data = request.get_json()

    try:
        task = task_service.create_task(data)

        return jsonify({
            "success": True,
            "data": task
        }), 201
    
    except ValueError as error:

        return jsonify({
            "sucess": False,
            "message": str(error)
        }), 400


@task_bp.route('/', methods=["GET"])
def get_tasks():
    pass


@task_bp.route('/<int:id>', methods=["GET"])
def get_task(id):
    pass


@task_bp.route('/<int:id>', methods=["DELETE"])
def delete_task(id):
    pass


@task_bp.route('/<int:id>', methods=["PUT"])
def update_task(id):
    pass


@task_bp.route('/<int:id>', methods=["PATCH"])
def patch_task(id):
    pass