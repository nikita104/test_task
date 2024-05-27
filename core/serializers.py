from re import split
from rest_framework import serializers

from core import models
from core import consts


class Worker(serializers.Serializer):
    full_name = serializers.CharField(label='ФИО')
    department = serializers.CharField(label='Название отдела')
    gender = serializers.ChoiceField(label='Пол', choices=consts.GENDER_CHOICE)

    last_name = serializers.CharField(label='Фамилия', required=False)
    first_name = serializers.CharField(label='Имя', required=False)
    middle_name = serializers.CharField(label='Отчество', required=False)

    def validate(self, data):
        try:
            data['last_name'], data['first_name'], *data['middle_name'] = tuple(split(' ', data['full_name']))
            return data
        except Exception as ex:
            raise serializers.ValidationError(f'Ошибка: {ex.args}')


class Department(serializers.ModelSerializer):
    worker_count = serializers.SerializerMethodField()
    male = serializers.SerializerMethodField()
    famale = serializers.SerializerMethodField()

    class Meta:
        model = models.Department
        fields = '__all__'

    def get_worker_count(self, obj: models.Department) -> int:
        return obj.worker_count

    def get_male(self, obj: models.Department) -> int:
        return obj.male

    def get_famale(self, obj: models.Department) -> int:
        return obj.famale
