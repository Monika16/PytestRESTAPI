**API Automation Framework**
Overview

This project is an API automation testing framework built using Python, Pytest, and the Requests library. It automates CRUD (Create, Read, Update, Delete) operations for the Todo API provided by Pixegami.

The framework follows a modular structure by separating API methods, test data, configuration, and test cases, making it easy to maintain and extend.

**Technologies Used**
* Python 3.x
* Pytest
* Requests
* UUID
* Pytest Fixtures

**Project Structure**
```
todo_api_project/
│
├── api/
│   ├── routes.py
│   └── task_api.py
│
├── data/
│   └── payloads.py
│
├── tests/
│   ├── test_create_task.py
│   ├── test_update_task.py
│   ├── test_delete_task.py
│   └── test_list_task.py
│
├── utils/
│   └── config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
**Framework Design**

_**API Layer**_

Contains reusable methods for interacting with the REST API.

**_Example methods:_**

* create_task()
* update_task()
* get_task()
* delete_task()
* list_tasks()

**Data Layer**

Generates dynamic request payloads using UUIDs so that every test executes with unique data.

**Test Layer**

Contains independent test cases for each API functionality.

**_Current tests include:_**

* Create Task
* Update Task
* List Tasks
* Delete Task

**Configuration**

The Base URL is stored separately in utils/config.py to simplify environment changes.

**Test Scenarios**

**_Create Task_**
* Create a new task
* Verify status code
* Retrieve the task
* Validate task content and user ID

**_Update Task_**
* Create a task
* Update task content
* Verify update
* Validate updated fields

**_List Tasks_**
* Create multiple tasks
* Retrieve all tasks for a user
* Validate the number of tasks returned

**_Delete Task_**
* Create a task
* Delete the task
* Verify it no longer exists

**Features**
* Modular project structure
* Reusable API client
* Dynamic test data generation
* Pytest fixtures
* Easy maintenance
* Independent test cases
* HTML reporting support
* Scalable architecture

**Requirements**
* pytest
* requests
* pytest-html


