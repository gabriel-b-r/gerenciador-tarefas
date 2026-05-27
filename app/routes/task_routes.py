from flask import Blueprint, jsonify, request

task_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')

@task_bp.route('/', methods=["POST"])
def create_tasks():
    data = request.get_json()
    return jsonify(data)


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