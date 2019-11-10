from django.urls import path
from url_shortener import views

urlpatterns = [
    path('url/create', views.UrlCreate.as_view()),
    path('url/<int:pk>', views.UrlDetail.as_view()),
]
