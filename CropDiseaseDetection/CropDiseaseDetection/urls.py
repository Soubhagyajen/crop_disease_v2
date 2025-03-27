"""
URL configuration for CropDiseaseDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import landing_page,blog_list, add_blog,blog_detail,delete_blog

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing'),  # New landing page at /
    path('predictor/', include('predictor.urls')),  # App URLs
    path('about/', views.about, name='about'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    # path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/add/', add_blog, name='add_blog'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path("blog/delete/<int:blog_id>/", delete_blog, name="delete_blog"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)