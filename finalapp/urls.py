from . import views
from django.urls.conf import path

urlpatterns = [

    path('',views.index,name='index'),
    path('books',views.books,name='books'),
    path('delete',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]