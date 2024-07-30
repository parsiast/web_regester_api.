from .views import postlist, postdetail
from django.urls import path

urlpatterns= [
    path('', postlist.as_view()),
    path('<int:pk>/', postdetail.as_view()),
]