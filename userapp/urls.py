from . import views
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^$',views.register, name="register"),
    url(r'^login/',views.login, name="login"),
    url(r'^logout/',views.logout, name="logout"),
    ]