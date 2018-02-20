from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiClient()
try:
    api_response = api_instance.cpu_get()
    pprint (api_response)
except ApiException as e:
    print (" Exception when calling DefaultApi - > cpu_get : % s \ n " % e)
