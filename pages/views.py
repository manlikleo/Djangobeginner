from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs): #*args,**kwargs
    print(args,kwargs)
    print(request.user)
    # return HttpResponse ("<h1> Hello World Django </h1>") #string of html code
    return render(request,"home.html",{})



def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})


def services_view(request,*args,**kwargs):
    my_context = {
        "title": "this is about us",
        "my_number": 123,
        "my_list": ['Lagos','Abuja','Kano']

    }
    return render (request,"about.html",my_context)


def social_view (request,*args, **kwargs):
    return httpResponse("<h1> social page </h1>")