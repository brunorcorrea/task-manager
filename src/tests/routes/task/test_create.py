import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from fastapi.testclient import TestClient
from main import app
from routes import task

client = TestClient(app)

class TestCreateTask:

    def test_given_completed_task__when_create_task__then_return_ok(self):
        content = {
            "id": 1,
            "title": "Valid Task",
            "description": "Valid Task Description",
            "due_date": "2024-07-10",
            "completed": True,
            "completed_date": "2024-07-05"
        }
        response = client.post(task.CREATE_TASK_URL, json=content)

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "title": "Valid Task",
            "description": "Valid Task Description",
            "due_date": "2024-07-10",
            "completed": True,
            "completed_date": "2024-07-05"
        }

    def test_given_incomplete_task__when_create_task__then_return_ok(self):
        content = {
            "id": 1,
            "title": "Valid Incomplete Task",
            "description": "Valid Incomplete Task Description",
            "due_date": "2024-07-10",
            "completed": False
        }
        response = client.post(task.CREATE_TASK_URL, json=content)

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "title": "Valid Incomplete Task",
            "description": "Valid Incomplete Task Description",
            "due_date": "2024-07-10",
            "completed": False,
            "completed_date": None
        }
