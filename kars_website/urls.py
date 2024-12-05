"""
URL configuration for kars_website project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include # we need these functions to acces our static pages on the web server.
from kars import views #This statement imports views.py from kars app directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kars.urls')), # This line includes the urls.py from the kars app directory. The '' in the path makes sure your home page comes up without extra addressing
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This line makes Django serve static files from the media directory when DEBUG is True.

