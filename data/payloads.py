import uuid

def create_new_payload():
    return {
        "content": f"my test content is {uuid.uuid4().hex}",
        "user_id": f"test_user_{uuid.uuid4().hex}",
        "is_done": False
    }
    