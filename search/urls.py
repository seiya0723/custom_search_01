#TODO:デフォルトでは各アプリのurls.pyは存在しないので作成する。

from django.urls import path
from . import views

app_name    = "search"
urlpatterns = [ 
    path('', views.index, name="index"),
]

