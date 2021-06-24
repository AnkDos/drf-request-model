# drf-request-model
A request model decorator to validate the request at DRF APIView 

# Usage : 

Define your API Model like this:
```
     {
         "name" : RequestModel(data_type=str, regex=""),
         "mobile": RequestModel(data_type=int, regex="", required=False)
     }
```
Call the RequestModelValidator Decorator on the APIView methods to validate the API request on the basis of above model. Example attaced for the reference.
