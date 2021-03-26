from django.shortcuts import render
from websites.models import Website
def home_view(request):
    name="Welcome to"

    obj=Website.objects.all()

    context={
        'name':name,
        'obj':obj,
    }

    return render(request,'base.html',context)