from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

from servisformu.views import sayfayiyazdir, formdurumusorgula, xmlcikart




urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^kn/$', formdurumusorgula, name='formdurumusorgula'),

    url(r'^xml/$', xmlcikart, name='xml'),
    url(r'^urunler\.xml$', xmlcikart, name='urunlerxml'),
    url(r'^sitemap\.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^yazdir/([\w\-]+)/$', sayfayiyazdir, name='sayfayiyazdir'),

    url(r'^admin/', admin.site.urls),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

