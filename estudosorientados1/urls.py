"""estudosorientados1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from estudosorientados import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/curso/', views.curso_api, name='index'),
    url(r'^api/turma/', views.turma_api, name='index'),
    url(r'^api/periodo/', views.periodo_api, name='index'),
    url(r'^api/professor/', views.professor_api, name='index'),
    url(r'^api/disciplina/', views.disciplina_api, name='index'),
    url(r'^api/estudoOrientado/', views.estudoOrientado_api, name='index'),
    url(r'^api/imagem/(?P<professor>[0-9]+)/', views.imagem_api, name='index'),
    url(r'^admin/', admin.site.urls),
]
