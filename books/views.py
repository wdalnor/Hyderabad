from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Book, Author, likes
from django.contrib.auth import authenticate, login 
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from books.forms import ContactForm, bookForm
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib import messages
from django.conf import settings
from .forms import UserForm
from django.contrib.auth.models import User
from django.db.models import F
import datetime
from django.utils import timezone
from django.db.models import Count



def userlogin(request):

    errors = []

    if request.method=='POST':
        

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return  HttpResponseRedirect('/books/')
            else:
                errors.append(" Sorry your acount is disapled")
                return render(request, 'books/login.html', {'errors': errors})
        else:
            errors.append("invalid login details")
            return render(request, 'books/login.html', {'errors': errors})
    else:
        return render(request, 'books/login.html', {'errors': errors})




def books_list(request):
    
    message = "No Books Yet To Display"
    number_of_likes = 0
    books_list = Book.objects.order_by('-publicatin_date')[:5]
    for bok in books_list:
        number_of_likes = Book.objects.prefetch_related('likes').count()
        #login_count = User.objects.filter(last_login__startswith=timezone.now().date()).count()# in this line i count number of users who logged in tody and i can then just passed it to the dic
        return render(request, 'books/index.html', {'books_list': books_list, 'number_of_likes':number_of_likes,})
    return render_to_response("books/index.html",{"message":message}, context_instance = RequestContext(request))


def book_detail(request, id):

    number_of_likes = 0
    book = get_object_or_404(Book, pk=id)
    b_auth = book.authors.all()
    number_of_likes = book.likes_set.all().count()  
    book.views = book.views + 1
    book.save()
   
    return render(request, 'books/book_detail.html', {'book':book,'number_of_likes':number_of_likes,'b_auth':b_auth})


def like_this_book(request, book_id):
    
    new_like, created = likes.objects.get_or_create(user=request.user, book_id=book_id)

    if not created: #user already liked this boook
        messages.add_message(request, messages.SUCCESS, 'YOU HAVE already liked this book')
        return HttpResponseRedirect('/books')
        
    else:
       # if request.method == 'GET':
          #  book_id = request.GET['book_id']   
        
       
        messages.add_message(request, messages.SUCCESS, 'YOU HAVE SUCCESSFULY liked this book')
        return HttpResponseRedirect('/books')



def add_book(request):
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.add_message(request , messages.SUCCESS,'YOU HVE SSUCCESSFULY ADD A BOOK')
            
            return redirect('/books')
        else:
            print form.errors
    else:
        form = bookForm()

    return render(request,'books/add_book.html',{'form':form})

def update_book(request, book_id):

    updated_book = get_object_or_404(Book, id=book_id)
    form = bookForm(request.POST or None , instance = updated_book) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/books')

    context = {
        'title':updated_book.title, 
        'authors':updated_book.authors,
        'publisher':updated_book.publisher,
        'publicatin_date':updated_book.publicatin_date,
        'form':form,
        }
    messages.add_message(request, messages.SUCCESS, 'YOU HAVE UPDATED THE BOOK INF SUCCESSFULY')
    return render(request,'books/add_book.html',context)


def conform_delete(request, book_id):
    obj = get_object_or_404(Book, id=book_id)
    number_of_likes = obj.likes_set.all().count() 
    if request.method =="POST":
        obj.delete()
        messages.add_message(request, settings.DELETE_MESSAGE, "YOU HAVE DELETED THIS BOOK")
        return HttpResponseRedirect('/books/')
    context = {
    "object": obj ,
    "number_of_likes":number_of_likes,
    }
    return render(request, "books/delete_conform.html", context)



def search(request):

    errors = []
    
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("please type something to search for")
        elif len(q) > 11:
            errors.append("you can't search for more than 10 charcaters")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', 
                {'books':books, 'query': q})
    return render(request, 'books/search_form.html',
        {'errors': errors,})

def like_this_book(request, book_id):

    new_like, created = likes.objects.get_or_create(user=request.user, book_id=book_id)
    if not created:
        messages.add_message(request, messages.SUCCESS, 'YOU HAVE already liked this book')
        return HttpResponseRedirect('/books')
        
    else:
        # here we should let the user like this book and register that
        messages.add_message(request, messages.SUCCESS, 'YOU HAVE SUCCESSFULY liked this book')
        return HttpResponseRedirect('/books')
    '''
    this is a view to count num of likes but it is not yet finsh
    book_id = None
    if request.method == 'GET':
        book_id = request.GET['book_id']
    likes = 0
    if book_id:
        book = get_object_or_404(Book, id=int(book_id))
        if book:
            likes = book.likes + 1
            book.likes = likes
            book.save()
            return HttpResponseRedirect('/books')
'''

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'someEmail@gmail.com'),
                ['siteowner@external.com']
            #    cd.get('email', <a class="reference external" href="mailto:'noreplay%40examble.com">'noreply@example.com</a>'),
             #   [<a class="reference external"href="mailto:'siteowner%40examble.com">'siteowner@examble.com</a>'],
            )
            return HttpResponseRedirect('/contact/thanks/')

    else:
        form = ContactForm(
            initial={'subject': 'I love you'}

         )
    return render(request, 'books/contact_form.html', {'form': form,'ip_add':request.META['REMOTE_ADDR']})



def register(request):

    # a boolean value telling the template that the registration was successful
   # set to false initailly. code changes value to true whenregistration succeeds . 

    #if request.session.test_cookie_worked():
      #  print " >>>> TEST COOKIE WORKED "
        

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        


        #if user_form.is_valid() and profile_form.is_valid():

        user = user_form.save()

        # Now we hash the password with the set_password method . 
        # once hashed  we can update the user object

        user.set_password(user.password)

        user.save()

            # Now sort out the userprofile instance
            # once hashed , we can update the user object

            # this delay saving the model until we are ready to avoid integrity problems.


           
           
            #did the user provides a profile picture?
           #if so , we need to set the user attribute ourselves, we set commit =False.
         
           

        return HttpResponseRedirect('/books/')


        registered = True

     


    else:
        user_form = UserForm()
       

    return render(request, 'books/register.html', {'user_form': user_form,'registered': registered })


def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse(" you are logged in ")
        else:
            return HttpResponse("please login now ")
    request.session.set_test_cookie()
    return render(request, 'books/login.html')
    '''
    user_id = int(request.POST['id'])
    member = User.objects.get(id=user_id);
    if member.password == request.POST['password']:
        request.session['user_id'] = member.id
        returnHttpResponse("you are in ")
    else:
        return returnHttpResponse(" your username or password is incorrect")

   

'''









                    
   

