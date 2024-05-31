from flask import request, jsonify, send_from_directory
from .model import Task, db
from . import ma
from datetime import datetime
from marshmallow import ValidationError, validates, fields


class TaskSchema(ma.Schema):
    """Схема для сериализации и десериализации экземпляров."""
    class Meta:
        fields = ('id', 'title', 'task_info',
                  'created_at', 'updated_at', 'datetime_to_do')

    title = fields.String(required=True, validate=lambda s: len(s) > 0)
    task_info = fields.String(required=True, allow_none=True)
    datetime_to_do = fields.DateTime(required=True,)

    @validates('title')
    def validate_title(self, value):
        """Пользовательская валидация поля title"""
        if not value:
            raise ValidationError('Title не может быть пустым.')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


def init_routes(app):
    @app.route('/static/<path:path>')
    def sent_static(path):
        """Роут для проверки работы API."""
        return send_from_directory('./static/', path)

    @app.route('/', methods=['GET'])
    def hello_world():
        """Роут для проверки работы API."""
        return jsonify('Hello World!'), 200

    @app.route('/tasks/create/', methods=['POST'])
    def create_task():
        """Роут создания новой заметки."""
        try:
            data = task_schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_task = Task(**data)
        db.session.add(new_task)
        db.session.commit()

        return task_schema.jsonify(new_task), 200

    @app.route('/tasks/list/', methods=['GET'])
    def get_tasks():
        """Роут получения всех заметки."""
        tasks = Task.query.all()
        return tasks_schema.jsonify(tasks), 200

    @app.route('/tasks/<int:id>/', methods=['GET'])
    def get_task(id):
        """Роут получения заметки по ID."""
        task = Task.query.get_or_404(id)
        return task_schema.jsonify(task), 200

    @app.route('/tasks/<int:id>/update/', methods=['PATCH'])
    def update_task(id):
        """Роут обновления существующей заметки."""
        task = Task.query.get_or_404(id)
        try:
            data = task_schema.load(request.json,
                                    partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        for key, value in data.items():
            setattr(task, key, value)
        task.updated_at = datetime.now()

        db.session.commit()
        return task_schema.jsonify(task), 200

    @app.route('/tasks/<int:id>/', methods=['DELETE'])
    def delete_task(id):
        """Роут для удаления заметки."""
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
