from django.contrib import admin
from django.urls import path
from memo.views import (IndexClass,
                        LoadClass,
                        EditClass,
                        delete)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexClass.as_view(), name="index"),
    path("load/", LoadClass.as_view(), name="load"),
    path("edit/<uuid:pk>/", EditClass.as_view(), name="edit"),
    path("delete/<uuid:pk>/", delete, name="delete"),
    #path("signup/", SignupClass, name="signup")
]