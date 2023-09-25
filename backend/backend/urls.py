from django.urls import path, include
from rest_framework import routers
from books import views
from books.views import ListBooksViewSet
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BooksViewSet)



urlpatterns = [
    
    path('', include(router.urls)),
    path('list/', ListBooksViewSet.as_view(), name='list'),
    path('books-categery/', include('books.urls')),
    #path('books_router/', include(books_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
