import imp
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

import accounts.views

urlpatterns = [
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),

    
]