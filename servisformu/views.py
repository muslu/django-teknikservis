from django.shortcuts import render
from servisformu.models import ServisForm, Urunler




def sayfayiyazdir(request, idsi):

    formdurumu      =   ServisForm.objects.get(id = idsi)
    formbilgileri   =   Urunler.objects.filter(ServisFormu__id = idsi)

    return render(request, 'yazdir.html', {'formbilgileri': formbilgileri, 'formdurumu':formdurumu})
