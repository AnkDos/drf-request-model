"""
Created By : Ankur 
"""

import re
from collections import defaultdict
from functools import wraps
from copy import deepcopy


class RequestModel:
    """"""

    def __init__(self,*, data_type, required=True, regex=None, nested=None):
        """"""
        self.data_type = data_type
        self.required = required
        self.regex = regex
        self.nested = nested if nested else {}


class RequestModelValidator:
    """"""
    def __init__(self, model):
        """"""
        self.model = model
        self.request_data = None
        self.error_data = None

    def __call__(self, func):
        """"""
        @wraps(func)
        def wrapper(*args):
            """"""
            self.request_data = None
            self.error_data = defaultdict(set)
            self.json_segment = {}
            self.model_segment = {}
            request = args[1]
            if request.method == 'GET':
                self.request_data = request.query_params
            else:
                self.request_data = request.data
                
            self.request_data = dict(self.request_data)
            if 'application/json' not in request.headers.get('Content-type', ''):
                self.detect_unnecessary_keys()
                for key, value in self.model.items():
                    self.validate_querydict(
                        key, value, self.request_data.get(key))
            else:
                self.break_json(self.request_data)
                self.break_model(self.model)
                print(self.json_segment, self.model_segment)
                self.detect_unnecessary_keys_json()
                for key, value in self.model_segment.items():
                    self.validate_request(key, value, self.json_segment.get(key))
            if self.error_data:
                raise Exception(f"Invalid Request {self.error_data}")
            return func(*args)
        return wrapper
        
    def detect_unnecessary_keys(self):
        """"""
        unnecessary_key = set()
        for key, value in self.request_data.items():
            if key not in self.model:
                unnecessary_key.add(key)
        if unnecessary_key:
            raise Exception(f"Un-necessary Keys Present {unnecessary_key}")
    
    def detect_unnecessary_keys_json(self):
        """"""
        unnecessary_key = set()
        for key, value in self.json_segment.items():
            if key not in self.model_segment:
                unnecessary_key.add(key)
        if unnecessary_key:
            raise Exception(f"Un-necessary Keys Present {unnecessary_key}")
       
    def validate_querydict(self, key, model_value, request_value):
        """"""
        if isinstance(request_value, list):
            for data in request_value:
                self.validate_request(key, model_value, data)
        else:
            self.validate_request(key, model_value, request_value)
    
    def validate_request(self, key, model_value, request_value):
        """"""
        if model_value.required and not request_value:
            self.error_data['requiredValueMissing'].add(key)
            return
        if request_value:
            if not isinstance(request_value, model_value.data_type):
                self.error_data['invalidDatatype'].add(key)
                return
        if model_value.regex:
            if not re.match(re.compile(model_value.regex), request_value):
                self.error_data['regexValidationFailed'].add(key)
                return
    
    def break_json(self, request_value):
        """"""
        for key_, value_ in request_value.items():
            self.json_segment[key_] = value_
            if isinstance(value_, dict):
                return self.break_json(value_)
        
    
    def break_model(self, model):
        """"""
        for key_, value_ in model.items():
            self.model_segment[key_] = value_
            if value_.nested:
                return self.break_model(value_.nested)
