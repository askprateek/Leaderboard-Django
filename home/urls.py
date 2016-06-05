from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login' , {'template_name':'home/index.html'}),
    url(r'^$' , home_index)
]
