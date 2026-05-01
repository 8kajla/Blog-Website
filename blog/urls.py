from django.urls import path , include
from . import views
from .api_view import HelloWorld , PostView , AuthorView
from rest_framework import routers


urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('allblogs',views.blog,name='all_post'),
    path('allblogs/<slug:url>',views.blog_view,name='blog_url'),
    path('search/', views.search_blog, name='search_blog'),
    path('authors/',views.authors,name='authors'),
    path('authors/<slug:slug>',views.view_authors,name='author_url'),
    path('api/hello',HelloWorld.as_view()),
    path('api-auth/', include('rest_framework.urls'))
    ]


router= routers.SimpleRouter()
router.register('api/post',PostView , basename='post')


urlpatterns += router.urls

authors = routers.SimpleRouter()
authors.register('api/author',AuthorView)


urlpatterns += authors.urls