import pytest

from api.task_api import TaskApi


@pytest.fixture
def task_api():
    return TaskApi()