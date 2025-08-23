from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
# Create your views here.
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = EmployeeForm()
        return render(request, 'create.html', {'form' : form})
    
def delete_employee(request):
    