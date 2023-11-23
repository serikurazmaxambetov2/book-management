from django.urls import path
from api.views import BookDetail, BookListCreate

urlpatterns = [
	path('books/', BookListCreate.as_view()),
	path('books/<int:pk>/', BookDetail.as_view())
]