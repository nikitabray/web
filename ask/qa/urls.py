from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    path('', mainpage, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('question/<int:question_id>/', question, name='question'),
    path('ask/', postform , name='ask'),
    path('popular/', popular, name='popular'),
    path('new/', test, name='new'),
]
