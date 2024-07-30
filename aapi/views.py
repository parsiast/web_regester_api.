from aapi.models import Post
from aapi.serializers import PostSerializer
from rest_framework import generics , permissions
from .permissions import IsAuthorOrReeadOnly


class postlist(generics.ListCreateAPIView):
    permission_classes= (permissions.AllowAny,)
    queryset= Post.objects.all()
    serializer_class=PostSerializer

class postdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= (IsAuthorOrReeadOnly,)
    queryset= Post.objects.all()
    serializer_class=PostSerializer


    