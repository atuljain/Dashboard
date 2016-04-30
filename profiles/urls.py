from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^list/$', 'profiles.views.profiles_list', name='profiles_list'),

]
