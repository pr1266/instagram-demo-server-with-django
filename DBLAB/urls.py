from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from test1 import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url('game/', views.GameListAPIView.as_view()),
    url(r'game/(?P<id>[\w-]+)/$', views.GameDetailAPIView.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
]