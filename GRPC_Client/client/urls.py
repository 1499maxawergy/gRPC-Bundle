from django import views
from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('index', views.indexView),
    path('login', views.loginView),
    path('check', views.loginCheck, name='loginCheck'),
    path('reg', views.regView),
    path('regManip', views.regDo, name='regDo'),
    path('delete', views.deleteView),
    path('delManip', views.deleteDo, name='deleteDo'),
    path('update', views.updateView),
    path('updateManip', views.updateDo, name='updateDo')
]