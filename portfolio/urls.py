"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from portfolio_website.views import home_view , contact_view , log_in , all_project , ProjectDetailView, dashboard_view, tester
from django.contrib.sitemaps.views import sitemap
from portfolio_website.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('allproject/', all_project, name='all_project'),
    path('admin-login/', log_in, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('contact/', contact_view, name='contact'),
    path('tester/', tester, name='tester'),
    path('', home_view, name='home'),
    path('project_details/<int:pk>', ProjectDetailView.as_view() , name='projectdetails'),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
    ),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)