from data.payloads import create_new_payload

def test_create_task(task_api):
    payload = create_new_payload()
    create_response = task_api.create_task(payload)
    assert create_response.status_code == 200

    task_id = create_response.json()["task"]["task_id"]

    get_response = task_api.get_task(task_id)
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["content"] == payload["content"]
    assert data["user_id"] == payload["user_id"]

