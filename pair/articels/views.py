from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    review = Review.objects.all()
    context = {
        "review": review,
    }
    return render(request, "articels/index.html", context)


def new(request):
    return render(request, "articels/new.html")


def create(requset):
    title = requset.GET.get("title")
    content = requset.GET.get("content")

    Review.objects.create(title=title, content=content)

    # context = {
    #     "title": title,
    #     "content": content,
    # }

    return redirect("articels:index")


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "articels/detail.html", context)


def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "articels/edit.html", context)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content
    review.save()
    return redirect("articels:index")


def delete(requset, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect("articels:index")
