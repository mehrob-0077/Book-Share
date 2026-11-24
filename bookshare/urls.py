from django.urls import path
from .views import *

urlpatterns = [
    path("category/",CategoryListCreate.as_view()),
    path("category/<int:pk>",CategoryRetrieveUpdateDestroy.as_view()),
    path("city/",CityListCreate.as_view()),
    path("city/<int:pk>",CityRetrieveUpdateDestroy.as_view()),
    path("book/",BookListCreate.as_view()),
    path("book/<int:pk>",BookRetrieveUpdateDestroy.as_view()),
    path("trade/",TradeListCreate.as_view()),
    path("trade/<int:pk>",TradeRetrieveUpdateDestroy.as_view()),
    path("my_book/",MyBookList.as_view()),
    path("reviews/",ReviewListCreate.as_view())
]
