from django.shortcuts               import render, get_object_or_404
from django.http                    import HttpResponse
from .forms                         import BookFormDelete, LoginForm, UserRegistrationForm, BookForm
from .models                        import Book
from django.shortcuts               import redirect
from django.contrib.auth            import authenticate, login
from django.contrib.auth.decorators import login_required
import PIL.Image 

def base(request):
    return render(request, 'base.html', {})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane.')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
        else:
            form = LoginForm()
    return render(request, 'Biblioteka/account/login.html', {'form': form})

def dashboard(request):
    return render(request, 
                    'Biblioteka/account/dashboard.html', 
                    {'section': 'dashborad'})

def register(request):
    user_form = UserRegistrationForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 
                            'Biblioteka/account/register_done.html', 
                            {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
    return render(request, 'Biblioteka/account/register.html', {'user_form': user_form})

def books(request):
    latest_book_list = Book.objects.order_by('-pub_date')
    user_book_list = Book.objects.order_by('-user')
    context = {'latest_book_list': latest_book_list, 'user_book_list' : user_book_list}
    return render(request, 'Biblioteka/all_books.html', context)

@login_required
def book_new(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return render(request, 
                            'Biblioteka/account/new_book_done.html', 
                            {'book': book})
    else:
        form = BookForm()
    return render(request, 
                    'Biblioteka/account/new_book.html', 
                    {'form': form})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'Biblioteka/detail.html', {'book': book})


@login_required
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            if request.user == book.user:
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return render(request, 'Biblioteka/detail.html', {'book': book})
            else:
                return HttpResponse('To nie twoja książka.')
    else:
        form = BookForm(instance=book)
    return render(request, 'Biblioteka/account/edit.html', {'form': form})

@login_required
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookFormDelete(request.POST, instance=book)
        if form.is_valid():
            if request.user == book.user:
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return render(request, 'Biblioteka/account/del_done.html', {'book': book})
            else:
                return HttpResponse('To nie twoja książka.')
    else:
        form = BookFormDelete(instance=book)
    return render(request, 'Biblioteka/account/del.html', {'form': form})