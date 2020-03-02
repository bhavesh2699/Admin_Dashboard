from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^accounts/register$", views.register,name="register"),
    url(r"^login$", views.login,name="login"),
    url(r"^accounts/logout$", views.logout,name="logout"),
    url(r'^admin$',views.admin,name="admin"),
    url(r'^delete/(?P<pk>\d+)$',views.delete,name="delete"),
    url(r"^student_login$", views.student_login,name="student_login"),
    url(r"^register_stud$", views.register_stud,name="register_stud"),
    url(r'^$',views.index,name="index"),
    #url(r"^admin/MyView$", views.MyView,name="MyView"),

]
