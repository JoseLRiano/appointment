from django.conf.urls import url
from . import views

app_name = 'appointmenthome'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.InfoView.as_view(), name='info'),
    url(r'user/add/$', views.UserCreate.as_view(), name='user-add'),
]