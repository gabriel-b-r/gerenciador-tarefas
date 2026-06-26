from app.services import task_service

def test_get_tasks_returns_empty_list(app):
    with app.app_context():
        response = task_service.get_tasks()

        assert response == []


def test_get_tasks_returns_tasks_list(app, created_task):
    with app.app_context():
        created_task

        response = task_service.get_tasks()

        assert response == [
            {
                "id": 1,
                "title": "Task",
                "description": "Testing",
                "priority": "LOW",
                "status":  "PENDING"
            }
        ]
        