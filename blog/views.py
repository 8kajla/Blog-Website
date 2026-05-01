from django.shortcuts import render
from django.http import Http404 ,HttpResponseRedirect
from .models import Post , Author
from django.db.models import Q, Count
from .forms import CommentForm
from django.urls import reverse


# Create your views here.




def home_page(request):
     f_list= Post.objects.all().order_by("-date")[:2]

     return render(request,'blog/index.html', {"blog":f_list})

def blog(request):
    post_list = Post.objects.all()
    return render(request,'blog/allpost.html',{"blog":post_list})




def blog_view(request,url):
    res_blog =  Post.objects.get(slug=url)
    form_data = CommentForm
    all_comments = res_blog.comments.all()
    if request.method =="POST":
        comment_data = request.POST
        form = CommentForm(comment_data)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=res_blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_url' ,args=[res_blog.slug]))
        return render(request, 'blog/posts.html', {'blog': res_blog, 'comments': form,'comment':all_comments})

    try:
        return render(request, 'blog/posts.html', {'blog': res_blog,'form':form_data,'comments':all_comments})
    except Exception:
        raise Http404()


def search_blog(request):
    query = request.GET.get('q', '').strip()

    results=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
    return render(request, 'blog/search-result.html', {
        'blog': results,
        'search_query': query
    })

def authors(request):
    res = Author.objects.annotate(blog_count=Count('post'))
    return render(request,'blog/authors.html',{'author':res})

def view_authors(request,slug):
    author = Author.objects.get(slug_author=slug)
    posts = Post.objects.filter(author=author)
    return render(request,'blog/view_author.html',{"author":author,"blog":posts})
