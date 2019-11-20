from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_word_book=Book.objects.all().filter(title__contains="Djangos' book").count()
#    num_word_types=Book.objects.all().filter(title__contains='book').genre.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_word_book':num_word_book},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by=2
 #   context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='book')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/locationclass

    def get_queryset(self):      
        return Book.objects.filter(title__icontains='book')[:5] # Get 5 books containing the title war


    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super(BookListView, self).get_context_data(**kwargs)
            # Create any data and add it to the context
            context['some_data'] = 'This is just some data'
            return context

class BookDetailView(generic.DetailView):
         model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by=2
 #   context_object_name = 'my_book_list'   # your own name for the list as a template variable
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/locationclass

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super(AuthorListView, self).get_context_data(**kwargs)
            # Create any data and add it to the context
            context['some_data'] = 'This is just some data'
            return context

class AuthorDetailView(generic.DetailView):
         model = Author
