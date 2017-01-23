from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from page.models import Category, Good


# Create your views here.
def index(request, id):
    cats = Category.objects.all().order_by("name")
    try:
        if id == None:
            cat = Category.objects.first()
        else:
            cat = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        raise Http404
    goods = Good.objects.filter(category=cat).order_by("name")
    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods})


def good(request, id):
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=id)
    except Good.DoesNotExist:
        raise Http404
    return render(request, "good.html", {"cats": cats, "good": good})
