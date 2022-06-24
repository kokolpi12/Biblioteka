from django.urls                import path
from django.contrib.auth        import views as auth_views
from . import views
from django.conf.urls.static    import static
from django.conf                import settings

urlpatterns = [
    path('', views.base, name='base'),
    # ex: Panel główny
    path('', views.dashboard, name='dashboard'),
    # ex: Dodawanie książki
    path('books/new', views.book_new, name='book_new'),
    # ex: Szczegóły o książce
    path('<int:book_id>/', views.detail, name='detail'),
    # ex: Wszystkie książki
    path('books/', views.books, name='books'),
    # ex: Edycja książki
     path('<int:pk>/edit/', views.edit, name='edit'),
    # ex: usuwanie książki
    #path('books/del/', views.delete, name='delete'),
    
    # Widoki logowania
    # ex: Rejestracja użytkownika
    path('register/', views.register, 
            name='register'),
    # ex: Logowanie
    path('login/', 
            auth_views.LoginView.as_view(), 
            name='login'),
    # ex: Po wylogowaniu
    path('logout/', 
            auth_views.LogoutView.as_view(), 
            name='logout'),
    # ex: Zmiana hasła
    path('password_change/', 
            auth_views.PasswordChangeView.as_view(), 
            name='password_change'),
    # ex: Po zmianie hasła
    path('password_change/done/', 
            auth_views.PasswordChangeDoneView.as_view(), 
            name='password_change_done'),
    # ex: Reset hasła
    path('password_reset/', 
            auth_views.PasswordResetView.as_view(), 
            name='password_reset'),
    # ex: Po resecie hasła
    path('password_reset/done/', 
            auth_views.PasswordResetDoneView.as_view(), 
            name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
            auth_views.PasswordResetConfirmView.as_view(), 
            name='password_reset_confirm'),
    path('reset/done/', 
            auth_views.PasswordResetCompleteView.as_view(), 
            name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)