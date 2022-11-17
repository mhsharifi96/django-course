from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'blog'
urlpatterns = [
    #simple view
    path('first',views.first_view),
    path('',views.PostsView.as_view(),name='main-page'),
    path('list',views.PostListView.as_view(),name='list-page'),
    path('post-detail/<int:pk>',views.post_detail,name='single-post'), #version 1,2
    # path('post-detail/<int:pk>',views.PostDetailView.as_view(),name='single-post'), #version 3-5
    path('category',views.CategoryView.as_view(),name='category'),

]
