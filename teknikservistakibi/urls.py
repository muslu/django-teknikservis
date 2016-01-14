from django.conf.urls import url
from django.contrib import admin

from servisformu.views import sayfayiyazdir

urlpatterns = [

    url(r'^yazdir/([\w\-]+)/$', sayfayiyazdir, name='sayfayiyazdir'),
    url(r'^admin/', admin.site.urls),

]

