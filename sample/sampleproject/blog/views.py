from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .sample_json import single_post , multi_posts

# request : https://docs.djangoproject.com/en/4.1/ref/request-response/

def first_view(request):
    return HttpResponse('<h1>this is first view</h1>')


def second_view(request):
    return HttpResponse('this is second view')


def third_view(request):
    # key value parameter
    # e.x : use search  => /search?q=maktab
    name = request.GET['name']
    print(name)
    return HttpResponse(f'hello , {name} , welcome to my site ')


def fourth_view(request,pk,title):
    # path parameter
    # e.x : use blog detail => blog/post/10 OR blog/post/title

    return HttpResponse(f'this is post {pk}')



def sample_html_view(request):
    # name = request.GET['name']
    template = """<html>
        <body>
            <h1>My First Heading</h1>
            <p>My first paragraph.</p>
            <p>your name is : {name}</p>

        </body>
    </html>"""
    return HttpResponse(template)



def sample_html_template_view(request):
    # first in app dir , create templates folder
    # second, import render form django.shortcuts
    # templates configurations : https://docs.djangoproject.com/en/4.1/topics/templates/#support-for-template-engines
    return render(request,'sample.html')



def post_detail(request):

    # context = {
    #     'title':'detail post',
    #     'text':'this is a sample text for showing on the templates :)',
    #     'author':{
    #         'first_name':'MH',
    #         'last_name':'sharifi',
    #         'register_date':'2022/01/02'
    #     }
    # }
    context = single_post

    return render(request,'post/detail.html',context)



def post_list (request):
    
    # context = {'posts':[
    #     {
    #         'title':'detail post 1',
    #         'text':'this is a sample text 1 for showing on the templates :)',
    #         'author':{
    #             'first_name':'MH',
    #             'last_name':'sharifi',
    #             'register_date':'2022/01/02'
    #             }
    #     },
    #     {
    #         'title':'detail post 2',
    #         'text':'this is a sample text  2for showing on the templates :)',
    #         'author':{
    #             'first_name':'MH',
    #             'last_name':'sharifi',
    #             'register_date':'2022/01/02'
    #             }
    #     },
    # ]}
    context = multi_posts

    # return render(request,'post/list.html',context)
    return render(request,'post/list_link.html',context)


def template_inheritance(request):
    # q= request.GET['q']
    # q = request.GET.get('q','default')
    return render(
        request,
        'inheritance.html',
        # {'q':q}
    )


# class View 

class AboutView(TemplateView):
    template_name = "about.html"


class PostsView(View):
    def get(self,request,*args, **kwargs):
        print('args',args)
        print('kwargs',kwargs)

        return render(request,'post/list_link.html',context=multi_posts)
    

    def post(self,request,*args, **kwargs):
        pass



import asyncio
class postViewAsync(View):
    async def get(self,request,*args, **kwargs):
        await asyncio.sleep(5)
        return HttpResponse("Hello async world!") 




