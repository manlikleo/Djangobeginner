from django.shortcuts import render


from .forms import ProductForm,RawProductForm
from .models import product



def render_initial_data(request):
    initial_data = {
        'title': "awesome title"
    }
    
    obj = product.objects.get(id=1)
    form = ProductForm(request.POST or None,initial = initial_data,instance=obj)
    context = {
        'form':form
    }
    return render(request,"products/product_create.html",context)








# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             product.objects.create(**my_form.cleaned_data)
        
#         # else:
#         #     print(my_form.errors)

#     context = {
#         "form": my_form
#     }
#     return render (request,"product/product_create.html",context)



# def product_create_view(request):
    
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     #producct.objects.create(title = my_new_litle)
#     context = {}
#     return render (request,"product/product_create.html",context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()


    context = {
        'form':form
    }
    return render (request,"product/product_create.html",context)



def product_detail_view(request):
    obj = product.objects.get(id=1)
    context = {
        'object':obj
        # 'title': obj.title,
        # 'Description': obj.Description
    }
    return render (request,"product/product_detail.html",context)


