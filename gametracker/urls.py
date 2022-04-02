from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bf1/', include('battlefield1.urls')),
    path('bf4/', include('battlefield4.urls')),
    path('bfh/', include('battlefield_hardline.urls')),
    path('data-analytics/', include('data_analytics.urls')),
    path('', include('home.urls'))
]
