from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.response import Response

from core import serializers
from core import models
from core import tasks


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
            obj = models.Department.objects.all()
            serializer = serializers.Department(obj, many=True)
            return Response(serializer.data, status=HTTPStatus.OK)

        except Exception as ex:
            error_msg = f'Неверный запрос: {ex.args}'
            return Response({'error_msg': error_msg}, status=HTTPStatus.BAD_REQUEST)
