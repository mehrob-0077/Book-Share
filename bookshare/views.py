from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CityListCreate(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class CityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class TradeListCreate(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializers

class TradeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializers

class MyBookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        query = super().get_queryset()
        print(self.request.user)
        return query.filter(owner=self.request.user)


class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = Review.objects.select_related('trade', 'author', 'user')
        user_id = self.request.query_params.get('user')
        if user_id:
            query = query.filter(user_id=user_id) if user_id.isdigit() else query.none()
        return query


