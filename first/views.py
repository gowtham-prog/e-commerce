from django.shortcuts import redirect,render
from django.http.response import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

from django.urls import *
from . models import *
# Create your views here.
def index(request):
    product =Products.objects.all()
    return render(request,"first/index.html",{
        "p":product,
    })
def post(request):
     if request.method=="POST":
         pro=Products()
         pro.Title=request.POST["Title"]
         pro.Description=request.POST["Description"]
         pro.Image=request.POST["Image"]
         pro.save()
         return HttpResponseRedirect (reverse("index"))
     else:
         return render(request, "first/form.html")
def about(request):
    return render(request,"first/about.html")
def contact(request):
    return render(request, "first/contact.html")
def home(request):
    return render(request,"first/index.html")
def addcomment(request,id):
    cUser=request.user
    product=Products.objects.get(id=id)
    if request.method == "POST":
        c=Comments.objects.create(user=cUser)
        c.Items=product
        c.comment=request.POST["comment"]
        c.save()
        return HttpResponseRedirect(reverse("fshow",args=[id]))
    else:
        return render(request,"first/comment.html",{
            "id":product.id
        })
def fshow(request,id):
    p=Products.objects.get(id=id)
    comments= Comments.objects.filter(Items=p).all()
    return render (request,"first/fshow.html",{
        "id": id,
        "product": p,
       "comments":comments,
    }) 
@login_required(login_url='/login')  
def wishlist(request,id):
    current=request.user
    try:
        instance= Wishlist.objects.get(user=current)
        return render(request, "first/index.html",{
            "p":instance.item.all(),
            "wishlist": True,
        })
    except Wishlist.DoesNotExist:
        return HttpResponse("NO items in your Wishlist")
    


  