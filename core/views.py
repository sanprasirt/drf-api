from django.shortcuts import render
from django.http import JsonResponse

# third party
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'jonh',
            'age': 23
        }
        return Response(data=data)

# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'jonh',
#         'age': 23
#     }
#     return JsonResponse(data) 