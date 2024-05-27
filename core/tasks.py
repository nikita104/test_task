from project import celery_app

from core import models


@celery_app.task()
def create_user(data: dict):
    department, _ = models.Department.objects.get_or_create(name=data['department'])
    models.Worker.objects.create(
        last_name=data['last_name'],
        first_name=data['first_name'],
        middle_name=data['middle_name'] or '',
        gender=data['gender'],
        department=department,
    )

