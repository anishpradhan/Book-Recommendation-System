"""BRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from .views import BookList, book_detail, rating_form, search_area
from account.views import registration_view, logout_view, login_view
urlpatterns = [
    path('', BookList.as_view(), name='home_api'),
    path('<item_id>/books_detail', book_detail, name="book_detail"),
    path('<item_id>/feedback', rating_form, name="rating_form"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('search/', search_area, name="search"),

]
