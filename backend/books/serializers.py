from django.contrib.auth.models import User, Group
from rest_framework import serializers
from books.models import Books_catlog

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']


class BooksSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Books_catlog
		fields = '__all__'
  
class BooksfilteredSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Books_catlog
		depth = 10
		fields = '__all__'
	