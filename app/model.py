from . import db
from datetime import datetime


class Task(db.Model):
    """Модель для предстваления в таблицу базы данных."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    task_info = db.Column(db.String(256), nullable=True)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now)
    datetime_to_do = db.Column(db.Date, default=datetime.now)

    def __init__(self, title, task_info, datetime_to_do):
        self.title = title
        self.task_info = task_info
        self.datetime_to_do = datetime_to_do
