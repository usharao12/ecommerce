from django.shortcuts import redirect, render

from app.models import Product

# Create your views here.
def index(request):
    data=Product.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        cost=request.POST.get('cost')
        query=Product(name=name,number=number,cost=cost)
        query.save()
        return redirect("/")
    return render(request,"index.html")
def update(request,id):
    d=Product.objects.get(id=id)
    context={"d":d}
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        cost=request.POST.get('cost')
        edit=Product.objects.get(id=id)
        edit.name=name
        edit.number=number
        edit.cost=cost
        edit.save()
        query=Product(name=name,number=number,cost=cost)
        query.save()
        return redirect("/")
    return render(request,"edit.html",context)
def delete(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    return redirect("/")