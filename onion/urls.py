from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('common/', include('common.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)