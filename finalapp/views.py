from django.shortcuts import render,redirect,get_object_or_404
from .models import Category
from .models import Book
from .forms import Add_book
from .forms import Add_category
from django.forms import ModelForm

def index(request):

    if request.method == 'POST':
        addbook = Add_book(request.POST, request.FILES)
        if addbook.is_valid():
            addbook.save()

    if request.method == 'POST':
        add_cat = Add_category(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    context = {

        'book':Book.objects.all(),
        'cat':Category.objects.all(),
        'form':Add_book(),
        'cat_sidebar':Add_category(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksolid': Book.objects.filter(status='solid').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookava': Book.objects.filter(status='available').count(),

    }

    return render(request,'pages/index.html',context)

def books(request):

    search =  Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)




    context = {

        'cat': Category.objects.all(),
        'book': search,
        'cat_sidebar': Add_category(),
    }



    return render(request,'pages/books.html',context)




def delete(request, id):
    context = {

        'cat': Category.objects.all(),

    }

    bk = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        bk.delete()
        return redirect('index')


    return render(request,'pages/delete.html',context)





def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        up_book = Add_book(request.POST,request.FILES,instance=book_id)
        if up_book.is_valid():
            up_book.save()
            return redirect('/')
    else:
        up_book = Add_book(instance=book_id)

    context = {

        'cat': Category.objects.all(),
        'form':up_book,
    }


    return render(request,'pages/update.html',context)