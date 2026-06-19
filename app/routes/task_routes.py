from flask import Blueprint, jsonify, request
from app.services import task_service
from app.models.task import Task

task_bp = Blueprint('tasks', __name__, url_prefix='/api/v1/tasks')

@task_bp.route('', methods=["POST"])
def create_task():
    data = request.get_json()

    try:
        task = task_service.create_task(data)

        return jsonify(
            task
            ), 201
    
    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400


@task_bp.route('/', methods=["GET"])
def get_tasks():

    try:

        tasks = task_service.get_tasks()

        return jsonify(
           tasks
        ), 200
    
    except Exception as error:

            return jsonify({
                "error": str(error)
            }), 500

@task_bp.route('/<int:task_id>', methods=["GET"])
def get_task(task_id):
    
    try:

        task = task_service.get_task_by_id(task_id)

        return jsonify(
            task
        ), 200
    
    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 404


@task_bp.route('/<int:task_id>', methods=["DELETE"])
def delete_task(task_id):
    
    try:

        task_service.delete_task(task_id)

        return "", 204

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 404


@task_bp.route('/<int:task_id>', methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    try:
        updated_task = task_service.update_task(task_id, data)

        return jsonify(
            updated_task
        ), 200
    
    except Exception as error:
        
        return jsonify({
            "error": str(error)
        }), 404


@task_bp.route('/<int:task_id>', methods=["PATCH"])
def patch_task(task_id):
    data = request.get_json()

    try:

        patched_task = task_service.patch_task(task_id, data)

        return jsonify(
            patched_task
        ), 200
    
    except Exception as error:
        
        return jsonify({
            "error": str(error)
        }), 404
