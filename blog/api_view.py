from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer,AuthorSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Post,Author
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import AuthorPermission


class PagePagination(PageNumberPagination):
    page_size= 3


class HelloWorld(APIView):
    def get(self,request):
        return Response({'Message':'Hello World'})


class PostView(ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly,AuthorPermission]
    queryset= Post.objects.all()
    serializer_class= PostSerializer
    pagination_class = PagePagination

    def perform_create(self,serializer):
        serializer.save(author=self.request.user.author)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.is_superuser:
            return Post.objects.all()

        if user.is_authenticated and hasattr(user, 'author'):
            return Post.objects.filter(author=user.author)

        return Post.objects.all()

class AuthorView(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class= AuthorSerializer