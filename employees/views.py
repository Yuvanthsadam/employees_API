from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import employees
from employees.models import User
from employees.serializers import UserSerializer


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        resp1 = {
            "code": 1,
            # "count": users_serializer.data.,
            "message": "success",
            "result": users_serializer.data
        }

        return Response(data=resp1, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp1 = {
                "code": 1,
                # "count": users_serializer.data.,
                "message": "success",
                "result": serializer.data
            }
            return Response(resp1)
        else:
            resp2 = {
                "code": 0,
                # "count": users_serializer.data.,
                "message": "Unsuccess",
                "result": serializer.errors
            }
            return Response(resp2)


class UserDetailView(APIView):

    def get(self, request, pk):
        try:
            users = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        users_serializer = UserSerializer(users)
        return Response(users_serializer.data)

    def put(self, request, pk):
        users = User.objects.get(pk=pk)
        users_serializer = UserSerializer(users, data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        else:
            return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        users = User.objects.get(pk=pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
