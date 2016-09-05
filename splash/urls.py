from django.conf.urls import url
from splash import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^photographers/', views.photographers, name="photographers"),
    url(r'^planners/', views.planners, name='planners'),
    url(r'^index_lp/', views.index_lp, name='index_lp'),
    url(r'^about/', views.about, name='about'),
]
