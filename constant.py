from .request_model import RequestModel
from django.core.files.uploadedfile import InMemoryUploadedFile

multipart_model_example = {
    "name": RequestModel(data_type=str),
    "profile_pic": RequestModel(data_type=InMemoryUploadedFile, required=False),
    "email": RequestModel(data_type=str,  regex="^[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9]+)+$"),
    "consent": RequestModel(data_type=bool, required=False),
    "mobile": RequestModel(data_type=str)
}

query_param_model_example = {
    "num": RequestModel(data_type=str, required=False)
}

simple_json_model_example = {
    "name": RequestModel(data_type=str, regex="^[a-zA-Z][a-zA-Z\' .,-]+[a-zA-Z]$"),
    "marks": RequestModel(data_type=list, required=False),
    "address": RequestModel(data_type=list),
    "int": RequestModel(data_type=int)
}

nested_json_model_example = {
    "name": RequestModel(data_type=str, regex="^[a-zA-Z][a-zA-Z\' .,-]+[a-zA-Z]$"),
    "marks": RequestModel(data_type=list, required=False),
    "address": RequestModel(data_type=dict, 
                                    nested={"street":RequestModel(data_type=int),
                                            "pincodes":  RequestModel(data_type=list),
                                            "corraddr": RequestModel(data_type=dict, nested={"street": RequestModel(data_type=str) ,"ank": RequestModel(data_type=int)})
                        
                                            }),
    "nk": RequestModel(data_type=str),
    "ta": RequestModel(data_type=dict, nested={"cool": RequestModel(data_type=bool) ,"aa": RequestModel(data_type=list)})
}
