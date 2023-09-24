from django.urls import path,include
from rest_framework import routers
from . views import BookDetailsAPIView

#router = routers.DefaultRouter()
#router.register(r'literature', views.LiteratureCategoryViewSet)
#router.register(r'non-fictinonon', views.Non_fictionCategoryViewSet)
#router.register(r'fictinonon', views.FictionCategoryViewSet)


urlpatterns = [
    path('bookdetails/<str:slug>', BookDetailsAPIView.as_view(), name='bookdetails'),
    
    
]
