def create_task(data):

    if not data.get("title"):
        raise ValueError("Title is required")

    task = {
        "id": data["id"],
        "title": data["title"],
        "description": data.get("description"),
        "priority": data.get("priority", "LOW"),
        "status": data.get("status", "PENDING"),
    }

    return task

