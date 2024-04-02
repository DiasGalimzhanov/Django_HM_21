from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoList.as_view(), name='home'),
    path('<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]