
from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_member, name="index"),
    path("info/<int:id>", views.view_detail, name="detail"),
    path("add/",views.view_add,name="create-member"),
    path("addpost/",views.add_post,name="add-post"),
    path("json/",views.json,name="json"),
    path("get/",views.getuser),
]