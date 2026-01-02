from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('portfolyo/', views.portfolio, name='portfolio'), # YENİ EKLENDİ
    path('proje/<int:pk>/', views.project_detail, name='project_detail'),
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    path('aydinlatma-metni/', views.kvkk, name='kvkk'),
    # Blog ve Kategori path'lerini sildik.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)