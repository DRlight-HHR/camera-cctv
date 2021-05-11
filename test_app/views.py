from django.shortcuts import render, get_object_or_404
from .models import book
from rest.models import camera

from django.shortcuts import redirect, Http404


def vid(request):
    query = camera.objects.all()
    data = {'data': query}
    return render(request, 'video.html', data)


def home(request):
    if request.user.is_authenticated is False:
        return redirect('/login/')
    r = request.user
    rr = r.username
    if request.method == 'POST':
        search_ = request.POST.get('search')
        query = book.objects.custom(search_)
        '''for i in query:
            print(i is None)'''
        data = {'data': query, 'name': rr}
        return render(request, 'book_home.html', data)
    query = book.objects.all()
    data = {'data': query, 'name': rr}
    return render(request, 'book_home.html', data)


def home_d(request, pk, name):
    if request.user.is_authenticated is False:
        return redirect('/login/')
    r = request.user
    rr = r.username
    if request.method == 'POST':
        search = request.POST.get('search')
        query = book.objects.custom(search)
        if query is None:
            return Http404('this page is not found')
        for i in query:
            print(i.id)
        data = {'data': query, 'name': rr}
        return render(request, 'book_home.html', data)
    query = get_object_or_404(book, name=name, pk=pk)
    data = {'data': query, 'name': rr}
    return render(request, 'home_d.html', data)


'''def home_d(request, pk):
    if request.user.is_authenticated is False:
        return redirect('/login/')
    r = request.user
    rr = r.username
    if request.method == 'POST':
        search = request.POST.get('search')
        query = book.objects.custom(search)
        if query is None:
            return Http404('this page is not found')
        for i in query:
            print(i.id)
        data = {'data': query, 'name': rr}
        return render(request, 'book_home.html', data)
    query = get_object_or_404(book, pk=pk)
    data = {'data': query, 'name': rr}
    return render(request, 'home_d.html', data)
'''
