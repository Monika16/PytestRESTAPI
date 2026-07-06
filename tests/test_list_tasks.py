from data.payloads import create_new_payload

def test_list_tasks(task_api):
    n = 3
    payload = create_new_payload()
    for _ in range(n):
        create_response = task_api.create_task(payload)
        assert create_response.status_code == 200

    user_id = payload["user_id"]
    list_task_response = task_api.list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    tasks = data["tasks"]
    assert len(tasks) == n