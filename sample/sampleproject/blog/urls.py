from django.urls import path
from django.views.generic import TemplateView
from . import views
# app_name = 'blog'
urlpatterns = [
    #simple view
    # path('first',views.first_view),
    path('',views.PostsView.as_view(),name='main-page'),
    path('list',views.PostListView.as_view(),name='list-page'),


    path('post/<int:pk>',views.PostDetailView.as_view(),name='single-post'),
    # path('post-detail/<int:pk>',views.PostDetailView.as_view(),name='single-post'),



]
