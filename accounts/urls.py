from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^login-user/$', 'accounts.views.login_user', name='login_user'),
    url(r'^logout-user/$', 'accounts.views.logout_user', name='logout_user'),
    # url(r'^forget-password/$', 'accounts.views.forget_password', name='forget_password'),
    # url(r'^reset-password/(?P<token>[a-zA-Z0-9]+)$', 'accounts.views.reset_password', name='reset_password'),

]
