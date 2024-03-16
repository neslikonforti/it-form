
from django.contrib import admin
from django.urls import path
from main.views import home_page,fill_page,edit_page,delete_page,confirm_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name="home"),
    path("fill/",fill_page,name="fill form"),
    path("edit/<int:person_id>",edit_page,name="edit"),
    path("delete/<int:person_id>",delete_page,name="delete"),
    path("delete/<int:person_id>/confirm",confirm_delete,name="confirm"),
]
