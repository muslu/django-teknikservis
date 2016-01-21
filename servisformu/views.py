# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from servisformu.models import ServisForm, Urunler


def formdurumusorgula(request):
    formno   =   request.POST.get('TakipNo', None)

    print formno

    try:
        formdurumu  =   ServisForm.objects.get(FormNo = formno)
        urunler     =   Urunler.objects.filter(ServisFormu__id = formdurumu.id)
        htmltablo   = u"<table style='width:100%;'><tr><th style='width:40%;' align='left'>Ürün</th><th style='width:40%;' align='left'>NOT</th><th style='width:20%;' align='left'>Durum</th></tr>"

        for k in urunler:
            htmltablo += "<tr>"
            htmltablo += "<td align='left'>" + k.Cins.upper() + "(" + k.Marka.upper() + " " + k.Model.upper() + ")</td>"
            htmltablo += "<td align='left'>" + k.Not + "</td>"
            htmltablo += "<td align='left'>" + k.Durum.Durumu + "</td>"
            htmltablo += "</tr>"
        htmltablo += "</table>"
        return HttpResponse(htmltablo)
    except:
        return HttpResponse("Form no bulunamadı!")
    return HttpResponse("Form no bulunamadı!")


def sayfayiyazdir(request, idsi):
    formdurumu      =   ServisForm.objects.get(id = idsi)
    formbilgileri   =   Urunler.objects.filter(ServisFormu__id = idsi)
    return render(request, 'yazdir.html', {'formbilgileri': formbilgileri, 'formdurumu':formdurumu})


def xmlcikart(request):
    tumformlar      =   ServisForm.objects.order_by('-KayitTarihi')
### Tüm servis formlarını kayıt tarihlerini sondan başa doğru sıralayarak 2 tanesini al. Yani son 2 kaydı al
    return render(request, 'formlar.xml', {'tumformlar': tumformlar}, content_type="application/xml")
### tumformlar adında toparladığımız son 2 kaydı formlar.xml dosyasına gönderiyoruz.
### Bu arada gönderdiğimiz dosyanın türü xml
### eski versiyonlarda mime_type olarak kullanılmalı
###  "application/xml" de kullanılabilir

def xmlcikart(request):
    tumformlar      =   ServisForm.objects.order_by('-KayitTarihi')

    from django.core.urlresolvers import resolve
    ### isterseniz yukarıya tamımlayabilirsiniz.
    GelenUrl = resolve( request.path_info ).url_name

    if GelenUrl == "urunlerxml":
        print tumformlar
        tumformlar  =   tumformlar[0:1]
        print tumformlar
        ### tumformlar bir liste olduğu için 1 kayıt al diyebilir ve tekrar aynı isimle tanımlayabiliriz

    return render(request, 'formlar.xml', {'tumformlar': tumformlar}, content_type="application/xml")




def test(request):



    list1       =   ['muslu', 'yuksektepe']
    list2       =   ['digerliste1', 'digerliste2']
    string      =   "bu bir string"
    integer     =   35

    return render(request, 'test.html', {
                                            'list1': list1,
                                            'list2':list2,
                                            'string':string,
                                            'integer':integer
                                        },
                  )

