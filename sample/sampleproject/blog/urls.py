from django.urls import path
from django.views.generic import TemplateView
from . import views
# app_name = 'blog'




urlpatterns = [
    #simple view
    path('',views.first_view),
    path('second',views.second_view),
    path('third',views.third_view), 
    # path('fourth/<int:pk>',views.fourth_view),
    path('fourth/<str:search>',views.fourth_view),
    path('fourth/<int:pk>/<str:title>',views.fourth_view),
    path('sample-html',views.sample_html_view),
    path('smaple-template',views.sample_html_template_view),
    # -------------------
    path('post-detail/',views.post_detail),
    path('posts',views.post_list),
    # path('post-detail/',views.post_detail,name='post_detail'),
    # path('posts',views.post_list,name='post_list'),
    #-------------------
    # path('about/', TemplateView.as_view(template_name="about.html")),  #OR
    path('about/', views.AboutView.as_view()), 
    path('posts-class/',views.PostsView.as_view()),
    #-------------------
    path('posts-async',views.postViewAsync.as_view()),
    


]
