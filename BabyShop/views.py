from django.shortcuts import render, redirect
from .models import Product, Author
from .forms import ProductForm
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def index(request):
    product = Product.objects.all()
    return render(request, "BabyShop/index.html", {"product_list": product})

def edit(request, pk):
    try:
        post = Product.objects.get(id=pk)

        if request.method == "POST":
            post.title = request.POST.get("title")
            post.author = request.POST.get("content")
            post.page = request.POST.get("page")
            post.author = request.POST.get("wtitten")

            post.save()
            return HttpResponseRedirect("/BabyShop")
        else:
            return render(request, "shop/edit.html", {"post": post})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, pk):
    try:
        post = Product.objects.get(id=pk)
        if post.user == request.user:
            post.delete()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseNotFound("<h2>У вас нет прав на удаление</h2>")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")