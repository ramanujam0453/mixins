from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^emp/$', views.EmpList.as_view()),
    url(r'^emp/(?P<pk>[0-9]+)', views.EmpDetails.as_view()),
]
