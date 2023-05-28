from django.shortcuts import render, HttpResponse, redirect
from books.models import Books


def get_all_books(request):
    all_books = Books.objects.all()
    return  render(request,'index.html', {"message":"add books",'all_books':all_books })

def get_single_book(request,id):
    book = Books.objects.get(pk=id)
    return render(request,'index.html',{'message':'one entity','book':[book]})

