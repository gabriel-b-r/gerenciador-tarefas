from flask import Blueprint, jsonify, request
from app.services import task_service
from app.models.task import Task
from app.validators.task_validator import validate_content_type

task_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')

@task_bp.route('', methods=["POST"])
def create_task():
    validate_content_type(request)

    data = request.get_json()

    task = task_service.create_task(data)

    return jsonify(
        task
        ), 201


@task_bp.route('', methods=["GET"])
def get_tasks():

    tasks = task_service.get_tasks()

    return jsonify(
        tasks
    ), 200
    

@task_bp.route('/<int:task_id>', methods=["GET"])
def get_task(task_id):
    task = task_service.get_task_by_id(task_id)

    return jsonify(
        task
    ), 200

@task_bp.route('/<int:task_id>', methods=["DELETE"])
def delete_task(task_id):
    task_service.delete_task(task_id)

    return "", 204


@task_bp.route('/<int:task_id>', methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    updated_task = task_service.update_task(task_id, data)

    return jsonify(
        updated_task
    ), 200
    


@task_bp.route('/<int:task_id>', methods=["PATCH"])
def patch_task(task_id):
    data = request.get_json()

    patched_task = task_service.patch_task(task_id, data)

    return jsonify(
        patched_task
    ), 200

