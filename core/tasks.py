from project import celery_app

from core import models


@celery_app.task()
def create_user(data: dict):
    department = models.Department.objects.get(name=data['department'])
    models.Worker.objects.create(
        last_name=data['last_name'],
        first_name=data['first_name'],
        middle_name=data['middle_name'] or '',
        gender=data['gender'],
        department=department,
    )

