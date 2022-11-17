from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from django.views import View
from django.http import Http404
import json
from django.urls import reverse,reverse_lazy


from .models import Post,Category,Comment

# request : https://docs.djangoproject.com/en/4.1/ref/request-response/

def first_view(request):
    return render(request,'index.html',{})



class PostsView(View):

    def get(self,request,*args, **kwargs):
        # get list of posts
        # posts = Post.objects.filter(title__startswith='s')
        posts = Post.objects.all()
        category = Category.objects.all()
        
        context = {'posts':posts,'category':category}
        return render(request,'main.html',context)
    

class PostDetailView(DetailView):
    model = Post
#     template_name = 'single-post.html'
#     context_object_name = 'post'


    

class PostListView(ListView):
    model = Post
    # queryset = Post.objects.all()[:2]
    context_object_name = 'posts'
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        
        return context




# Post method and form Django

#version 1
# def post_detail(request,pk):

#     post = get_object_or_404(Post,pk=pk)

#     comments = Comment.objects.all() 

#     context = {
#         'post':post,
#         'comments':comments
#     }

#     return render(request,'single-post.html',context)

# version 2
# def post_detail(request,pk):
#     print('---------------------------------------')
#     print(request.method)
#     post = get_object_or_404(Post,pk=pk)
#     context= {
#         'post':post,
#         'comments':{}
#     }
#     if request.method == 'GET':

#         comments = Comment.objects.all() 
#         context['comments'] = comments
    
#     else :
        
#         print(type(request.body),':',request.body)
#         print(request.POST)
#         print('email :  ',request.POST.get('email',None))
#         # save comment 
#         comment = Comment(post=post,email=request.POST.get('email',None)
#         ,title=request.POST.get('title',None)
#         ,content= request.POST.get('content',None)).save()
#         return redirect(reverse('blog:single-post-def',args=[pk]))

#     return render(request,'single-post.html',context)


#version 3 - class view       
# class PostDetailView(View):
#     def get(self,request,*args, **kwargs):
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         comments = Comment.objects.all() 
#         context= {
#             'post':post,
#             'comments':comments
#         }
#         return render(request,'single-post.html',context)

#     def post(self,request,*args, **kwargs):
#         print(request.POST)
#         print('email :  ',request.POST.get('email',None))
#         # save comment 
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         comment = Comment(post=post,email=request.POST.get('email',None)
#         ,title=request.POST.get('title',None)
#         ,content= request.POST.get('content',None)).save()
#         return redirect(reverse('blog:single-post-def',args=[kwargs['pk']]))




# #version4  - add forms     
# from .forms import commentForm
# class PostDetailView(View):
    
#     def get(self,request,*args, **kwargs):
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         comments = Comment.objects.filter(pk = kwargs['pk']) 
#         form = commentForm()
#         context= {
#             'post':post,
#             'comments':comments,
#             'form':form
#         }
#         return render(request,'single-post.html',context)

#     def post(self,request,*args, **kwargs):
      
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         comments = Comment.objects.all() 
#         # save comment 
#         form = commentForm(request.POST)
#         print('form is valid : ',form.is_valid())
#         print(form.cleaned_data)
#         # # comment = Comment(post=post,email=request.POST.get('email',None)
#         # ,title=request.POST.get('title',None)
#         # ,content= request.POST.get('content',None)).save()
#         if form.is_valid():
#             print('form_is valid')
#             comment = Comment(**form.cleaned_data)
#             comment.post = post 
#             comment.save()
#             return redirect(reverse('blog:single-post',args=[kwargs['pk']]))
        
#         context= {
#             'post':post,
#             'comments':comments,
#             'form':form
#         }
        
#         return render(request,'single-post.html',context)

#version5  - add Modelforms     
from .forms import CommentModelForm
class PostDetailView(View):
    context = {}
    def get(self,request,*args, **kwargs):
        self.context['post'] = get_object_or_404(Post,pk=kwargs['pk'])
        self.context['comments'] = Comment.objects.all() 
        self.context['form'] = CommentModelForm()
        
        return render(request,'single-post.html',self.context)

    def post(self,request,*args, **kwargs):
       
        self.context['post'] = post = get_object_or_404(Post,pk=kwargs['pk'])
        self.context['comments'] = Comment.objects.all() 
        # save comment 
        self.context['comments'] = form = CommentModelForm(request.POST)
                
        if form.is_valid():
            print('form_is valid')
            comment_form = form.save(commit=False)
            # comment_form.post_id = kwargs['pk']
            comment_form.post = post
            comment_form.save()
            
            return redirect(reverse('blog:single-post',args=[kwargs['pk']]))
        
        return render(request,'single-post.html',self.context)



class CategoryView(CreateView):
    model = Category
    fields = '__all__' 
    # success_url = reverse_lazy('blog:category') # or add get_absolute_url in models

    # def get_context_data(self, **kwargs) :
    #     kwargs['object_list'] = Category.objects.order_by('-id')
    #     return super().get_context_data(**kwargs)


class CategoryUpdateView(UpdateView):
    pass


class CategoryDeleteView(DeleteView):
    pass




