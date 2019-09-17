from django.core.serializers import serialize
from django.http import HttpResponse
import json

class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        std_list=[]
        for obj in p_data:
            e_dict=obj['fields']
            std_list.append(e_dict)
        json_data=json.dumps(std_list)
        return json_data

class HttpResponseMixin(object):
    def render_to_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
