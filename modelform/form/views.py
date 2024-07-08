from django.shortcuts import render
from .models import StudentModel
from .forms import ModelForm
# Create your views here.
def student(request):
    if request.method=='POST':
        fm=ModelForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            rl=fm.cleaned_data['roll']
            ct=fm.cleaned_data['city']
            reg=StudentModel(name=nm,roll=rl,city=ct) 
            # reg=StudentModel(id=11,name=nm,roll=rl,city=ct)  update 
            # reg.save()
        
        # delete method in django
        # reg=StudentModel(id=13)
        # reg.delete()
        # fm=ModelForm()
    else:
        fm=ModelForm()
    return render(request,'app/base.html',{'fm':fm})
