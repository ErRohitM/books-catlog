from django.contrib.auth.models import User
from rest_framework import viewsets,generics,response
from rest_framework import permissions
from books.serializers import UserSerializer, BooksSerializer, BooksfilteredSerializer
from books.models import Books_catlog
from books.forms import add_book_form
import datetime
from django.shortcuts import render,redirect



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class BooksViewSet(viewsets.ModelViewSet):
	queryset = Books_catlog.objects.all()
	serializer_class = BooksSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListBooksViewSet(generics.ListCreateAPIView):
    
        queryset = Books_catlog.objects.all()
        serializer_class = BooksSerializer
       

class BookDetailsAPIView(generics.GenericAPIView):
    serializer_class = BooksSerializer
    
    def get(self, request, slug):
        
        query_set = Books_catlog.objects.filter(slug=slug).first()
        if query_set:
            
            return response.Responce(self.serializer_class(query_set).data)
        else:
            return response.Responce('Not found', status=status.HTTP_404_NOT_FOUND)
        
        