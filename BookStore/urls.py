"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp , name = 'signup'),
    path('signin/', views.SignIn , name = 'signin'),
    path('signout/',views.SignOut, name = 'signout'),
    path('list/', views.BookList , name = 'list'),
    path('detail/<int:book_id>/', views.BookDetail , name = 'detail'),
    path('books/<int:book_id>/buy/',views.addToCart ,name='book-buy'),
    path('create-book/', views.create , name = 'create'),
    path('update-book/<int:book_id>/', views.update , name = 'update'),
    path('delete-book/<int:book_id>/', views.delete , name = 'delete'),
    path('purchased-book/', views.purchasedBooks , name = 'purchased'),
    path('seller-sold-book/', views.sellerSoldBooks , name = 'soldBooks'),
    path('seller-book/', views.sellerBooks , name = 'sellerBooks'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)