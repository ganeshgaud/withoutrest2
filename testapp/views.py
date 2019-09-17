from django.shortcuts import render
from django.views import View
from .mixins import SerializeMixin,HttpResponseMixin
from .utils import is_json
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import EmployeeForm

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUD(SerializeMixin,HttpResponseMixin,View):
    def is_id_valid(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except ObjectDoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
        data=request.body
        json_data=is_json(data)
        if not json_data:
            json_data=json.dumps("Sorry please enter Valid Json Data!!!")
            return self.render_to_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.is_id_valid(id)
            if emp is None:
                json_data=json.dumps("Entered ID={} is not Available!!!".format(id))
                return self.render_to_response(json_data,status=400)
            json_data=self.serialize([emp,])
            return self.render_to_response(json_data)
        emp=Employee.objects.all()
        json_data=self.serialize(emp)
        return self.render_to_response(json_data)

    def post(self,request,*args,**kwargs):
        data=request.body
        json_data=is_json(data)
        if not json_data:
            json_data=json.dumps("Sorry please enter Valid Json Data!!!")
            return self.render_to_response(json_data,status=404)
        emp=json.loads(data)
        form=EmployeeForm(emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Updated Successfully!!!")
            return self.render_to_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=403)

    def put(self,request,*args,**kwargs):
         data=request.body
         json_data=is_json(data)
         if not json_data:
             json_data=json.dumps("Sorry please enter Valid Json Data!!!")
             return self.render_to_response(json_data,status=404)
         pdata=json.loads(data)
         id=pdata.get('id',None)
         if id is None:
             json_data=json.dumps("Please Enter ID to update")
             return self.render_to_response(json_data,status=400)
         emp=self.is_id_valid(id)
         if emp is None:
            json_data=json.dumps("Entered ID={} is not Available!!!".format(id))
            return self.render_to_response(json_data,status=400)
         provided_data=json.loads(data)
         available_data={
         'ename':emp.ename,
         'eaddr':emp.eaddr,
         'esal':emp.esal,
         'ecell_no':emp.ecell_no
         }
         available_data.update(provided_data)
         print(available_data)
         form=EmployeeForm(available_data,instance=emp)
         if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Updated Successfully!!!")
            return self.render_to_response(json_data)
         if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=403)



    def delete(self,request,*args,**kwargs):
        data=request.body
        json_data=is_json(data)
        if not json_data:
            json_data=json.dumps("Sorry please enter Valid Json Data!!!")
            return self.render_to_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps("Please Enter ID to Delete")
            return self.render_to_response(json_data,status=400)
        emp=self.is_id_valid(id)
        if emp is None:
           json_data=json.dumps("Entered ID={} is not Available!!!".format(id))
           return self.render_to_response(json_data,status=400)
        status,deleted_item=emp.delete()
        if status==1:
            json_data=json.dumps("Record with ID={} Deleted Successfully!!!".format(id))
            return self.render_to_response(json_data)
        json_data=json.dumps("Record Not Deleted properly Please try after sometime")
        return self.render_to_response(json_data,status=400)
