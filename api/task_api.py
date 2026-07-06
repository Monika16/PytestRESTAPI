import requests
from utils.config import URL

class TaskApi:
    def create_task(self, payload):
        return requests.put(URL + "/create-task", json=payload)

    def update_task(self,payload):
        return requests.put(URL + "/update-task", json=payload)

    def get_task(self,task_id):
        return requests.get(URL + f"/get-task/{task_id}")

    def list_tasks(self,user_id):
        return requests.get(URL + f"/list-tasks/{user_id}")

    def delete_task(self,task_id):
        return requests.delete(URL + f"/delete-task/{task_id}")