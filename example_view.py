from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .request_model import RequestModelValidator
from .constant import *

class ReqeuestModelView(APIView):
    """"""
    @RequestModelValidator(query_param_model_example, 'query_params')
    def get(self, request):
        """Query Param Example """
        print(request.query_params)
        return Response({'foo': 'bar'})

    @RequestModelValidator(multipart_model_example)
    def post(self, request):
        """Multipart Form Data Example"""
        print(request.data)
        return Response({'foo': 'bar'})
    
    @RequestModelValidator(payload_query_param, 'query_params')
    @RequestModelValidator(simple_json_model_example)
    def put(self, request):
        """Simple JSON Example, USE it like this when you have both query params and payload"""
        print(request.data)
        print(request.query_params)
        return Response({'foo': 'bar'})
    
    @RequestModelValidator(nested_json_model_example)
    def patch(self, request):
        """Nested Json Example"""
        print(request.data)
        return Response({'foo': 'bar'})
