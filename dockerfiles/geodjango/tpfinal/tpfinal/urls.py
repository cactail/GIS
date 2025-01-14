"""tpfinal URL Configuration

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

from geo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ejemplo4/$', views.render_html_01),
    url(r'^ejemplo7/$', views.render_html_02),
    url(r'^consulta$', views.consulta),
    url(r'^agregar$', views.agregar_elementos),
    url(r'^mostrarcapa$', views.mostrar_capa_editable),
    # index
    url(r'^$', views.index),
]
