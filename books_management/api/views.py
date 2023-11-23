from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from api.serializers import BookSerializer
from api.models import Book

class BaseBookView(generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	renderer_classes = [JSONRenderer]

class BookListCreate(BaseBookView, generics.ListCreateAPIView):
	pass

class BookDetail(BaseBookView, generics.RetrieveUpdateDestroyAPIView):
	pass