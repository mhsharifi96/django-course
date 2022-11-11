from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from django.http import Http404


from .models import Post

# request : https://docs.djangoproject.com/en/4.1/ref/request-response/

def first_view(request):
    return render(request,'single-post.html',{})



class PostsView(View):

    def get(self,request,*args, **kwargs):

        # get list of posts
        posts = Post.objects.all()
        context = {'posts':posts}
        return render(request,'main.html',context)


class PostDetailView(View):

    def get(self,request,*args, **kwargs):
        # get one post
        pk = kwargs['pk']
        print(kwargs)
        try:    
            post = Post.objects.get(pk=pk)  # or
        except Post.DoesNotExist:
            # post = {}
            raise Http404("No MyModel matches the given query.")
        # post = get_object_or_404(Post,pk=pk)

        context = {'post':post}
        return render(request,'single-post.html',context)


# class PostDetailView(DetailView):
#     model = Post

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'single-post.html'
#     context_object_name = 'post'


class PostListView(ListView):
    model = Post
    

# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'main.html'
#     queryset = Post.objects.all()[:2]

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['now'] = 'now'
#     #     return context

    


        



