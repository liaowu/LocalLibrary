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
        ]
