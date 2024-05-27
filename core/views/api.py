from http import HTTPStatus
from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.response import Response

from core import serializers
from core import models
from core import tasks
from core import consts


class UserViewSet(viewsets.ViewSet):
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        try:
            serializer = serializers.Worker(data=request.data)
            serializer.is_valid(raise_exception=True)

            tasks.create_user.apply_async(kwargs={'data': serializer.data},
                                          queue='priority_high')

        except Exception as ex:
            error_msg = f'Неверный запрос: {ex.args}'
            return Response({'error_msg': error_msg}, status=HTTPStatus.BAD_REQUEST)

        return Response('ок', status=HTTPStatus.OK)

    def list(self, request, *args, **kwargs):
        try:
            obj = models.Department.objects.annotate(
                worker_count=Count('workers__pk'),
                male=Count('workers__gender', filter=Q(workers__gender=consts.MALE)),
                famale=Count('workers__gender', filter=Q(workers__gender=consts.FEMALE))
            )
            serializer = serializers.Department(obj, many=True)
            return Response(serializer.data, status=HTTPStatus.OK)

        except Exception as ex:
            error_msg = f'Неверный запрос: {ex.args}'
            return Response({'error_msg': error_msg}, status=HTTPStatus.BAD_REQUEST)
