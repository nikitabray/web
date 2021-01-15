from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    path('', mainpage, name='home'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/<int:question_id>/', question, name='question'),
    path('ask/', test, name='ask'),
    path('popular/', popular, name='popular'),
    path('new/', test, name='new'),
]
