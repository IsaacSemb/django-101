from django.shortcuts import render
from django.http import HttpResponse
from .models import Book 
from django.db.models.aggregates import Count, Min, Max, Avg, Sum

# for objects that dont exist
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# return some html from a render 
def intro (request):
    return HttpResponse('<h1>welcome to the book keeper</h1>')

# returning an entire template
def welcome(request):
    return (render(request, 'welcome.html'))

# returning an template with some logic
def welcome(request):
    name = 'Isaac Ssembuusi'
    for i in range(5):
        print(i)
    
    return (render(request, 'welcome.html',{'name':name}))


# managers and querysets
def get_books(request):
    
    # all_books
    books = Book.objects.all()
    book_count = Book.objects.count()
    
    sliced_books = books[0:10]
    
    book_id = 5
    try:
        get_id = Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        get_id = f'The object with id {book_id} doesnt exist'
    
    # better way of getting it
    book_getter = Book.objects.filter(pk=5).exists()
    
    # filtering books
    filtered_books1 = Book.objects.filter(year_of_publication__gt=2003) 
    filtered_books2 = Book.objects.filter(year_of_publication__range=(1994, 1998))
    filtered_books3 = Book.objects.filter(year_of_publication__lt=1993)
    
    # <field_name>__icontains = 'string'  --- icontain
    filtered_books4 = Book.objects.filter(title__icontains='romance')
    filtered_books5 = Book.objects.filter(title__istartswith='man')
    filtered_books6 = Book.objects.filter(title__iendswith='man')
    
    # combining filters
    filtered_books7 = Book.objects.filter(title__istartswith='a', year_of_publication__gt=1996 )
    filtered_books7 = Book.objects.filter(title__istartswith='a').filter(year_of_publication__gt=2000 )
    
    
    # using the OR operator we using Q objects
    from django.db.models import Q
    filtered_books8 = Book.objects.filter( Q(title__istartswith='v') |  Q(year_of_publication__gt=2002)  )
    filtered_books8 = Book.objects.filter( Q(title__istartswith='a') &  Q(year_of_publication__gt=2000)  )
    
    # negating queries with ~ means opposite
    filtered_books8 = Book.objects.filter( Q(title__istartswith='a') &  ~Q(year_of_publication__lt=1996)  )
    
    # using F objects helps to compare aspects of 2 fields in the same table
    
    # sorting elements in django ( DEFAULT IS ASCENDING ORDER)
    filtered_books9 = Book.objects.filter(year_of_publication__range=(1994, 1998)).order_by('title')
    filtered_books9 = Book.objects.filter(year_of_publication__range=(1994, 1998)).order_by('year_of_publication')
    
    # add a negative to reverse sorting
    filtered_books9 = Book.objects.filter(year_of_publication__range=(1994, 1998)).order_by('-year_of_publication')
    filtered_books9 = Book.objects.filter(year_of_publication__range=(1994, 1998)).order_by('-title')
    
    # IF YOU DONT WANT TO USE A NEGATIVE YOU CAN USE REVERSE FUNCTION
    filtered_books9 = Book.objects.filter(year_of_publication__range=(1994, 1998)).order_by('title').reverse()
    
    # OTHERS INCLUDE
    # earliest 
    # latest
    
    context = { 
            "all_books" : books,
            'sliced_books':sliced_books,
            'counter':book_count,
            'get_by_id':get_id,
            'book_getter' : book_getter,
            'book_filter1' : filtered_books1,
            'book_filter2' : filtered_books2,
            'book_filter3' : filtered_books3,
            'book_filter4' : filtered_books4,
            'book_filter5' : filtered_books5,
            'book_filter6' : filtered_books6,
            'book_filter7' : filtered_books7,
            'book_filter8' : filtered_books8,
            'book_filter9' : filtered_books9,
            'limiting_results1' : Book.objects.all()[7:13],
            'limiting_results1' : Book.objects.all()[7:15],
            
            
            # return only wanted values in the query or table
            'chosen_fields1': Book.objects.values('ISBN','id', 'year_of_publication' )[:3],
            
            # return tuples
            'chosen_fields2': Book.objects.values_list('ISBN','id', 'year_of_publication' )[:3],
            
            # aggregating objects ( count min max avg sum)
            'aggregation1': Book.objects.aggregate(Count('id')),
            'aggregation2': Book.objects.aggregate(Sum('year_of_publication')),
            'aggregation3': Book.objects.aggregate(Max('year_of_publication')),
            'aggregation4': Book.objects.aggregate(Avg('year_of_publication'))
            
            
            
            
            
            
            }
    
    return (render(request, 'show_books.html', context))