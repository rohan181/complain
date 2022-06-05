from django.urls import path


from .views import HomeView,PostView,PostCreateView,PostUpdateViewadmin,PostUpdateView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/',PostUpdateView.as_view(), name='complaint-update'),
    path('post/<int:pk>/',PostUpdateViewadmin.as_view(), name='complaint-updateadmin'),
    
]