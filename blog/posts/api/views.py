from rest_framework import permissions, generics
from .serializers import PostSerializer
from rest_framework import status
from posts.models import Post

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer