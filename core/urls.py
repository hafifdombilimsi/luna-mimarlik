"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import home, project_detail, about, contact,category_projects, blog_index, blog_detail, kvkk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ana sayfa ('') bizim home fonksiyonuna gitsin
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('hakkimizda/', about, name='about'), # <-- Yeni eklediğimiz satır
    path('iletisim/', contact, name='contact'),
    path('kategori/<int:pk>/', category_projects, name='category_projects'),
    path('blog/', blog_index, name='blog_index'),           # Blog ana sayfası
    path('blog/<int:pk>/', blog_detail, name='blog_detail'), # Blog detay sayfası
    path('aydinlatma-metni/', kvkk, name='kvkk'),
]

# Resimlerin görünmesi için gerekli ayar (Sadece geliştirme modunda)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


