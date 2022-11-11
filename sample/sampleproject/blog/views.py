from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from django.http import Http404


from .models import Post,Category

# request : https://docs.djangoproject.com/en/4.1/ref/request-response/

def first_view(request):
    return render(request,'index.html',{})



class PostsView(View):

    def get(self,request,*args, **kwargs):
        # get list of posts
        # posts = Post.objects.filter(title__startswith='s')
        posts = Post.objects.all()
        category = Category.objects.all()
        context = {'post':posts,'category':category}
        return render(request,'main.html',context)
    



# class PostDetailView(View):

#     def get(self,request,*args, **kwargs):
#         # get one post
#         print(kwargs)
#         pk = kwargs['pk']
#         try:
#             post = Post.objects.get(pk=pk)  # or
#         except Post.DoesNotExist:
#             raise Http404("No Post matches the given query.")
       

#         # post = get_object_or_404(Post,pk=pk)

#         context = {'post':post}
#         return render(request,'single-post.html',context)


# class PostDetailView(DetailView):
#     model = Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'single-post.html'
    context_object_name = 'post'


# class PostListView(ListView):
#     # model = Post
#     queryset = Post.objects.all()[:2]
#     context_object_name = 'posts'
#     template_name = 'main.html'
    

class PostListView(ListView):
    model = Post
    # queryset = Post.objects.all()[:2]
    context_object_name = 'posts'
    template_name = 'main.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        
        return context



    


        



