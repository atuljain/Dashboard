from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView, TemplateView, RedirectView


urlpatterns = [
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
]
