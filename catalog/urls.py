from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
#    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
#    re_path(r'^book/(?P<stub>[-\w]+)$', views.BookDetailView.as_view(), name='book-detail'),
# Reused view with different urls and parameters:
#    path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
#    path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
        ]
urlpatterns += [
        path('mybooks/',views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),
        ]
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
