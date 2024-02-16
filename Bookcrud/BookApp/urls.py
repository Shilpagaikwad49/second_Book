
from django.urls import path
from BookApp import views
urlpatterns = [
    path('home',views.homePage),
    path('addbook',views.addbook),
    path('delete/<bookid>',views.deleteBook),
    path('update/<bookid>',views.updateBook)
]