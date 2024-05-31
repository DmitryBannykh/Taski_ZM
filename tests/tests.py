import requests
from datetime import datetime
URL = 'http://127.0.0.1:5000'


def test_create_task():
    """Тест для создания таска. Создается две записи,
    в терминал выводится только одна."""
    data = {
        "title": "Task 1",
        "task_info": "Description 1",
        "datetime_to_do": str(datetime.now())
    }
    data1 = {
        "title": "Task 2",
        "task_info": "Description 2",
        "datetime_to_do": str(datetime.now())
    }
    result = requests.post(f'{URL}/tasks/create/', json=data)
    print((f"test_create_task:"), result.status_code, result.text)
    requests.post(f'{URL}/tasks/create/', json=data1)


def test_tasks_list():
    """Тест для вывода списков всех тасков."""
    result = requests.get(f'{URL}/tasks/list/')
    print((f"test_tasks_list:"), result.status_code, result.text)


def test_tasks_id(id):
    """Тест для вывода задачи по id."""
    result = requests.get(f'{URL}/tasks/{id}/')
    print((f"test_tasks_id:"), result.status_code, result.text)


def test_tasks_update(id):
    """Тест для изменения задачи по id."""
    data = {
        "title": "Redefining a task",
        "task_info": "Redefining the description",
        "datetime_to_do": "2024-06-23 00:00:00"
    }
    result = requests.patch(f'{URL}/tasks/{id}/update/', json=data)
    print("test_tasks_update:", result.status_code, result.text)


def test_tasks_delete(id):
    """Тест для удаления задачи по id."""
    result = requests.delete(f'{URL}/tasks/{id}/')
    print((f"test_tasks_delete{id}:"), result.status_code, result.text)


if __name__ == "__main__":
    test_create_task()
    test_tasks_list()
    test_tasks_id(1)
    test_tasks_update(2)
    test_tasks_delete(2)  # При вторичном и последующем запуске тестов,
    # у test_tasks_delete() требуется менять ID(параметр) на большее значение.
