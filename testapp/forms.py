from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal<2000:
            raise forms.ValidationError("Salary above 2000 is eccepted???")
        return inputsal

    # def clean_ecell_no(self):
    #     inputcellno=self.cleaned_data['ecell_no']
    #     count=0
    #     while inputcellno>0:
    #         count=count+1
    #         inputcellno=inputcellno//10
    #     if count<10:
    #         raise forms.ValidationError("Cell No more than 10 digits is not accepted##")
    #     return inputcellno

    class Meta:
        model=Employee
        fields='__all__'
