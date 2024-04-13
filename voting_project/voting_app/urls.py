from django.urls import path
from . import views
from voting_app.views import signup
# from voting_app.views import IndexView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('questions/',views.questions, name='question'),
    path('questions/', views.questions, name='questions'),
    # path ('ques/',views.ques,name='ques'),
    # path ('pollswebsite/',views.pollswebsite,name='pollswebsite'),
    path('pages/index/', views.index, name='index'),
    

    

]
