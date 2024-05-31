## Описание
Тестовое задание для добавления, чтения, редактирования и удаления задач.

## Технологии.

- Flask
- SQLAlchemy
- Sqlite
- Python

## Запуск проекта.

1. Склонируйте текущий репозиторий на свой компьютер.
```bash
git clone git@github.com:DmitryBannykh/Taski_ZM.git
```
2. Создайте виртуальное окружение проекта и активируйте его
```bash
python -m venv venv
source venv/bin/activate
```
3. Установить зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
4. Запустите приложение.
```bash
python app.py
```
5. После запуска предусмотрена тестовая проверка эндпоинтов. Папка tests, файл test.py 
```bash
cd tests
python tests.py
```
В терминал будет выведены все операции с элементами.
При вторичном и последующем запуске тестов, у test_tasks_delete() и test_tasks_update() требуется менять ID(параметр) на большее значение.
(Смотри файл /tests/test.py строки 57-58)


# Автор Dmitry Bannykh. 
([Dmitry Bannykh](https://github.com/DmitryBannykh))