from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .request_model import RequestModelValidator
from .constant import *

class ReqeuestModelView(APIView):
    """"""
    @RequestModelValidator(query_param_model_example)
    def get(self, request):
        """Query Param Example """
        return Response({'foo': 'bar'})

    @RequestModelValidator(multipart_model_example)
    def post(self, request):
        """Multipart Form Data Example"""
        return Response({'foo': 'bar'})
    
    @RequestModelValidator(simple_json_model_example)
    def put(self, request):
        """Simple JSON Example"""
        return Response({'foo': 'bar'})
    
    @RequestModelValidator(nested_json_model_example)
    def patch(self, request):
        """Nested Json Example"""
        return Response({'foo': 'bar'})
