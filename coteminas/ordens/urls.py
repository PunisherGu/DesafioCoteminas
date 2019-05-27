from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.csv, name='csv'),	
    #url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),

]