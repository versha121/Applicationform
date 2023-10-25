
"""d"""
from  django.shortcuts import render

print("Hello0-----")

def jobapplication(request):
    print("hello")
    if request.method=='POST':
        v1 = request.POST.get("fullname",0)
        v2 = request.POST.get("lastname",0)
        v3 = request.POST.get("dateofbirth",0)
        
        return render(request,'registration.html',{"output":f"Values is {v1+v2} and DOB is {v3}"})
    return render(request,'jobapplication.html')
    
def registration(request):
    if request.method=='POST':
        v1 = request.POST.get("fullname",0)
        v2 = request.POST.get("lastname",0)
        v3 = request.POST.get("dateofbirth",0)
        return render(request,'registration.html',{"output":f"Values is {v1+v2} and DOB is {v3}"})
    return render(request,'registration.html')

