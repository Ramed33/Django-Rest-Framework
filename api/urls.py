from rest_framework.urlpatterns import format_suffix_patterns 
from django.urls import path
from . import views

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_creation = views.PostViewSet.as_view({
    'post': 'set_comment'
})


urlpatterns = [ 
   path('v1/posts/', post_list, name='post_list'),
   path('v1/post/<pk>/', post_detail, name='post_detail'), 
   #path('v1/post/(?P<pk>[0-9]+)/comment/', comment_creation, name='comment_creation'),
   path('v1/post/<pk>/comment/', comment_creation, name='comment_creation'),
]


urlpatterns = format_suffix_patterns(urlpatterns)