from django.conf.urls import url, include
from payligent import views
from django.conf import settings
from django.conf.urls.static import static

import registration.backends.simple.views

app_name='payligent'

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^sendmessage/$', views.send_message, name='send_message'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
	url(r'^signup/(?P<level>[\w\-]+)/$', views.signup, name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)