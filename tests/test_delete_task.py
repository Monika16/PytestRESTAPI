from data.payloads import create_new_payload

def test_delete_task(task_api):
    payload = create_new_payload()
    create_task_response = task_api.create_task(payload)
    assert create_task_response.status_code == 200
    create_task_data = create_task_response.json()
    task_id = create_task_data["task"]["task_id"]

    delete_task_response = task_api.delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = task_api.get_task(task_id)
    assert get_task_response.status_code == 404
