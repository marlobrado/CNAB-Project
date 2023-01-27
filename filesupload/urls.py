from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file),
    path("list/", views.ShopView.as_view()),
    

]
