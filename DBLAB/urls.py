from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from test1 import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #! GAME
    url(r'game/$', views.GameListAPIView.as_view()),
    url(r'game/(?P<id>[\w-]+)/$', views.GameDetailAPIView.as_view()),
    #! GAME ORDER
    url(r'gameorder/$', views.GameOrderListAPIView.as_view()),
    url(r'gameorder/(?P<id>[\w-]+)/$', views.GameOrderDetailAPIView.as_view()),
    #! TOKEN
    url(r'^api-token-auth/', obtain_jwt_token),
    # VIEWS : 
    url('pltGame/', views.GetPltGames),
    url('catGame/', views.GetCatGames),
    url('pltAcc/', views.GetPltAccessories),
    url('catAcc/', views.GetCatAccessories),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)