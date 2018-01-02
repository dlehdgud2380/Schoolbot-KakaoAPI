"""kap_yhbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from yhbot import views as yhbot_views

urlpatterns =  [
    url(r'^admin/', admin.site.urls),
    url(r'^keyboard/', yhbot_views.keyboard, name = 'keyboard'),
    url(r'^message', yhbot_views.answer, name = 'message'),
    url(r'^meal_parser/', yhbot_views.meal_parser, name = 'meal'),
    url(r'^img/(?P<pk>[0-9]+)/$', yhbot_views.schoolinfo_imgloader, name = 'school_info'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
